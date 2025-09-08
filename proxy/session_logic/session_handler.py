# imports to find other functions in project
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))


from session_types import *
from type_validation import *

# websockets imports
from websockets.legacy.server import WebSocketServerProtocol, serve # for websockets server websocket
from websockets import ClientProtocol # for websockets client

# other imports
from typing import Any, Union
import json
import asyncio # for timeouts


async def handle_session(name:str, ses:Session, actor_list, recv_queues, send_queues, types:dict, error_mode:str, timeout:float) -> End:
    '''
    Function that receives a session related to an actor, and checks said actor is going through the series of
    sessions as defined by the protocol.

        Args:
            name (str): Name of the actor the session belongs to
            ses (Session):
            actor_list (): __ that allows us to retrieve the websocket that belongs to a specific actor in the meeting
            recv_queues: queue function* that stores messages received by proxy and sent by a specific actor
            send_queues: ___ queue __ that stores all emssages too be sent to an actor
            types (dict): dict with all the json schemas referenced by type name, for checking the payload adheres to the defined type at runtime

        Returns:
            An End session, once it goes through all the other sessions.
    '''
    
    # initialize
    actual_session = ses
    doing:list[Choice | Rec] = [] # TODO: actually restrict sessions inside to only be choice or rec
    last_msg_name = None # so that labels of message don't need to be repeated twice if actor did a choice
    msg_name = None
    error = None
    branch = None
    choice_idx = 0

    try:
        while (not isinstance(actual_session, End)):

            print(f"carrying out ses {actual_session} for {name}") # debug
            match (actual_session):
                # -- Message sessions ---------------------------------------------------------------------------------------------------------------------------------
                case (Message()):
                    print(f"action name {actual_session.label}") # debug
                    match (actual_session.dir.dir):
                        case ("from"): # receive message from someone else
                            try:
                                msg = await send_queues[name].get()  # get message from queue

                                ok_payload = check_payload(msg, actual_session.payload, types)
                                print(f"checking payload in to") # debug
                                # if payload validation failed
                                if not ok_payload:
                                    print(f"Schema validation error at {actual_session.label.label}, expected type {actual_session.payload}") # debug
                                    if error_mode == "fatal":
                                        raise SchemaValidationError() # raise exception because if it only returns End() then other actors won't crash
                                    elif error_mode == "handle" and not error: # set error if mode is not "ignore"
                                        error = "wrongPayload"

                                await actor_list[name].send(msg) # finally send it
                                print(f"Message received by {name}, sent by {actual_session.actor}") # debug
                            except Exception as e:
                                print(f"from, {e}") # debug
                                return End()
                        case ("to"): # send message to someone else
                            try:
                                if last_msg_name: # message name was received by the choice block
                                    msg_name = last_msg_name
                                    last_msg_name = None # reset
                                else:
                                    # receive message, handle timeouts
                                    try:
                                        msg_name = json.loads(await asyncio.wait_for(recv_queues[name].get(), timeout=timeout))
                                        # msg_name = await recv_queues[name].get()
                                    except asyncio.TimeoutError:
                                        if error_mode == "fatal":
                                            raise Timeout()
                                        elif error_mode == "handle" and not error: # set error if mode is not "ignore"
                                            error = "timeout"
                                        

                                coincides = (msg_name == actual_session.label.label)
                                if not coincides:
                                    print(f"Wrong label at {actual_session.label.label}, got message name {msg_name}") # debug
                                    if error_mode == "fatal":
                                        raise WrongLabelError() # raise exception because if it only returns End() then other actors won't crash
                                    elif error_mode == "handle" and not error: # set error if mode is not "ignore" and a previous error hasn't been reported
                                        error = "wrongLabel"

                                msg = await recv_queues[name].get()  # get message from sender
                                ok_payload = check_payload(msg, actual_session.payload, types)
                                print(f"checking payload in from") # debug

                                # if payload validation failed
                                if not ok_payload:
                                    print(f"Schema validation error at {actual_session.label.label}, expected type {actual_session.payload}") # debug
                                    if error_mode == "fatal":
                                        raise SchemaValidationError() # raise exception because if it only returns End() then other actors won't crash
                                    elif error_mode == "handle" and not error: # set error if mode is not "ignore"
                                        error = "wrongPayload"
                                
                                print(f"{name} setting {msg_name}: {json.loads(msg)} for {actual_session.actor}")
                                await send_queues[actual_session.actor].put(msg)  # queue message for recipient (so we can send it to it when it is ready)
                                print(f"Message sent by {name} to {actual_session.actor}") # debug
                            except (SchemaValidationError, Timeout, WrongLabelError) as e:
                                print(f"In {name}, fatal: {e}")
                                raise e
                            except Exception as e:
                                print(f"In {name} session message, to, error: {e}")
                                raise e # debug
                        case _:
                            return End()
                    actual_session = actual_session.cont # update sessions to use in while loop
                # -- Choice sessions ---------------------------------------------------------------------------------------------------------------------------------
                case(Choice()):
                    try:
                        # case 1: the actor to whom this session belongs chooses branch
                        if actual_session.actor == name:

                            # report back if errors happened
                            if error_mode == "handle":
                                print(f"{name} checking for errors...") # debug
                                print(f"{error}")
                                branch = None
                                if error:
                                    if error in actual_session.errors:
                                        branch = error
                                    elif "error" in actual_session.errors:
                                        branch = "error"
                                    else:
                                        error = None
                                print(f"setting branch as {branch}")
                                    # notify choice actor if there was an error
                                await actor_list[name].send(json.dumps(branch)) # none if no error or ignore, or error type if error
                            
                            if not error: # if no error, we have to get selected branch from actor (if mode is not handle, error will be None anyways)
                                print(f"in {name}, waiting for non-error action label")
                                # 1: receive name of first message in selected branch
                                branch = json.loads(await recv_queues[name].get()) # is received directly from actor
                                print(f"{name}, got branch {branch}")
                                last_msg_name = branch
                            print(f"choice of {name}, chose branch {branch}") # debug
                            error = None # reset error in any case

                            # 2: send to involved parties
                            for act in actual_session.actors_involved:
                                if act != name:
                                    print(f"sending branch decision from {name} to {act}") # debug
                                    # will send index over, because label depnds on projected protocol
                                    for i in range (len(actual_session.alternatives)): # go through choice and get right index
                                        elem = actual_session.alternatives[i][0]
                                        if isinstance(elem, Message):
                                            if elem.label.label == branch:
                                                choice_idx = i
                                                break # TODO: breaks only for?? check
                                    await send_queues[act].put(json.dumps(choice_idx))     
                            doing.append(actual_session) # mark that you're carrying out choice session

                        # case 2: this actor RECEIVES a branch index
                        else:
                            choice_idx = json.loads(await send_queues[name].get()) # branch will be waiting in queue, will be an index 
                            doing.append(actual_session) # mark that you're carrying out choice session
                            print(f"{name} choice_idx = {choice_idx}") # TODO: erase
                            # if you branched to a choice, then send label to actor later (because you won't know until after)
                            # but if you branched to message or rec, send name of THOSE to actor! 
                            if actual_session.alternatives[choice_idx][0].kind in ["message", "rec"]:
                                print(f"actor {name} is supposed to get action label now")
                                await actor_list[name].send(json.dumps(actual_session.alternatives[choice_idx][0].label.label))
                            elif actual_session.alternatives[choice_idx][0].kind == "ref": # TODO: is this ok? ref vs rec in this case
                                await actor_list[name].send(json.dumps(actual_session.alternatives[choice_idx][0].name))
                        
                        # set for both cases
                        actual_session = actual_session.alternatives[choice_idx][0] # start with first action, others follow with cont

                    except Exception as e:
                        print(f"choice, {e}, actor fail:{name}") # debug
                        raise e
                # -- Ref sessions ---------------------------------------------------------------------------------------------------------------------------------
                case(Ref()):
                    print(f"doing ref {actual_session.name} in {name}") # debug
                    for item in reversed(doing): #take latest Rec session
                        if isinstance(item, Rec) and item.label == actual_session.name:
                            actual_session = item
                            break
                    try: 
                        pass
                    except Exception as e:
                        print(f"in {name}, ref problem, {e}") # debug
                        raise e
                # -- Rec sessions ---------------------------------------------------------------------------------------------------------------------------------
                case(Rec()):
                    # declare rec and go inside rec list to do actions
                    doing.append(actual_session)
                    actual_session = actual_session.actions[0]
                    try: 
                        pass
                    except Exception as e:
                        print(f"in {name} rec problem, {e}") # debug
                        raise e
                case _:
                    return End()
            # -- Handle None -------------------------------------------------------------------------------------------------------------------------------------
            # if it is the last action in rec or choice, do next session (cont) of rec/choice and close said rec/choice
            if not actual_session: # if actual session is None; a next cont indicates for choice and rec that their list of actions is over and we might close them
                actual_session = doing[-1].cont
                # print(f"replacing None ses with {type(doing[-1].cont)} from {type(doing[-1])} for actor {name}") # comment out to debug
                doing.pop()

        return End() # only returned when session is end
    except (SchemaValidationError, Timeout, WrongLabelError) as e:
        print(f"In {name}, fatal: {e}")
        raise e
    except Exception as e:
        raise e





