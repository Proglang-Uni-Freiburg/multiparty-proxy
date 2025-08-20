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
from typing import Any
import json


async def handle_session(name:str, ses:Session, actor_list, recv_queues, send_queues, types:dict) -> End:
    '''
    Function that receives a session related to an actor, and checks said actor is going through the series of
    sessions as defined by the protocol.

        Args:
            name (str): Name of the actor the session belongs to
            ses (Session):
            actor_list (): __ that allows us to retrieve the websocket to belongs to a specific actor in the meeting
            recv_queues: queue function* that stores messages received by proxy and sent by a specific actor
            send_queues: ___ queue __ that stores all emssages too be sent to an actor
            types (dict): dict with all the json schemas referenced by type name, for checking the payload adheres to the defined type at runtime

        Returns:
            An End session, once it goes through all the other sessions.
    '''
    
    # initialize
    actual_session = ses
    doing:list[Session] = [] # TODO: actually restrict sessions inside to only be choice or rec
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
                                await actor_list[name].send(msg) # finally send it
                                print(f"Message received by {name}, sent by {actual_session.actor}") # debug
                            except Exception as e:
                                print(f"from, {e}") # debug
                                return End()
                        case ("to"): # send message to someone else
                            try:
                                msg = await recv_queues[name].get()  # get message from sender
                                print(f"checking payload: {check_payload(msg, actual_session.payload, types)}") # for now print but later raise error if it returns False
                                await send_queues[actual_session.actor].put(msg)  # queue message for recipient (so we can send it to it when it is ready)
                                print(f"Message sent by {name} to {actual_session.actor}") # debug
                            except Exception as e:
                                print(f"to, {e}") # debug
                                return End()
                        case _:
                            return End()
                    actual_session = actual_session.cont # update sessions to use in while loop
                # -- Choice sessions ---------------------------------------------------------------------------------------------------------------------------------
                case(Choice()):
                    try:
                        # case 1: the actor to whom this session belongs chooses branch
                        if actual_session.actor == name:
                            # 1: receive branch index
                            branch = await recv_queues[name].get() # is received directly from actor
                            print(f"choice of {name}, chose branch {json.loads(branch)}") # debug
                            # 2: send to involved parties
                            for act in actual_session.actors_involved:
                                if act != name:
                                    print(f"sending branch decision from {name} to {act}") # debug
                                    await send_queues[act].put(branch)
                        # case 2: this actor RECEIVES a branch index
                        else:
                            print(f"{name} not deciding branch")
                            branch = await send_queues[name].get() # branch will be waiting to be sent in queue
                            await actor_list[name].send(branch) # directly send toa ctor through websockets

                        # for both, set sessions
                        doing.append(actual_session)
                        actual_session = actual_session.alternatives[json.loads(branch)][0] # start with first action, others follow with cont
                    except Exception as e:
                        print(f"choice, {e}, actor fail:{name}") # debug
                        return End()
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
                        print(f"ref problem, {e}") # debug
                        return End()
                # -- Rec sessions ---------------------------------------------------------------------------------------------------------------------------------
                case(Rec()):
                    # declare rec and go inside rec list to do actions
                    doing.append(actual_session)
                    actual_session = doing[-1].actions[0]
                    try: 
                        pass
                    except Exception as e:
                        print(f"rec problem, {e}") # debug
                        return End()
                case _:
                    return End()
            # -- Handle None -------------------------------------------------------------------------------------------------------------------------------------
            # if it is the last action in rec or choice, do next session (cont) of rec/choice and close said rec/choice
            if not actual_session: # if actual session is None; a next cont indicates for choice and rec that their list of actions is over and we might close them
                actual_session = doing[-1].cont
                # print(f"replacing None ses with {type(doing[-1].cont)} from {type(doing[-1])} for actor {name}") # comment out to debug
                doing.pop()

        return End() # only returned when session is end
    except Exception as e:
        print(f"prob in session: {e}")


