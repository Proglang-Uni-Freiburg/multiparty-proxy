import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from session_types import *
from type_validation import *
from websockets.legacy.server import WebSocketServerProtocol, serve # for websockets server websocket
from websockets import ClientProtocol # for websockets client
from typing import Any

import json

# proxy has to do the sending and receiving!!

# not used for now
async def send(actor_list, actor:str, message:Any, websocket:ClientProtocol|WebSocketServerProtocol): # message is an Any because we'll send a json
    # function s.d. an actor can send a message to another, because proxy has list of actors<->sockets
    # to will be actor's "nickname" -> have we added that to list? See how to!
    # correct kind of websocket; it should only be one type
    await actor_list[actor].send(message) # -> getting name from list will give back socket
    # but how does function know it's sending from proxy's side????



# suppose async because we're handling messages
async def handle_session(name:str, ses:Session, actor_list, recv_queues, send_queues, types) -> End: # does it actually always return End??
    # need proxy socket so we can se the send and receive functions from websockets??
    # we need the actor list so we can relate sockets to actor for the sending and receiving of messages?
    # initialize sessions
    # name is name of actor carrying ses out rn
    actual_session = ses
    print(f"in handler, {actual_session} for {name}") # debug
    doing:list[Session] = [] # actually restrict sessions inside to only be choice or rec
    
    
    while (not isinstance(actual_session, End)):
       
        # debug
        if not type(actual_session) == Ref:
            print(f"actual session: {actual_session}, cont: {actual_session.cont} in {name}")
        else:
             print(f"actual session: {actual_session} in {name}")

        print(f"carrying out ses {actual_session} for {name}")
        # print(payload) # debug
        match (actual_session):
            case (Message()):
                print(f"action name {actual_session.label}") # debug
                match (actual_session.dir.dir):
                    case ("from"): # receive message from someone else
                        try:
                            print(f"in {name} from {actual_session.actor}") # debug
                            msg = await send_queues[name].get()  # get message from queue
                            await actor_list[name].send(msg) # finally send it
                            print(f"Message received by {name}, sent by {actual_session.actor}") # to track what proxy is doing at moment -> could be removed
                        except Exception as e:
                            print(f"from, {e}") # debug
                            return End()
                    case ("to"): # send message to someone else
                        try:
                            print(f"in {name} to {actual_session.actor}") # debug
                            msg = await recv_queues[name].get()  # get message from sender
                            print(f"checking payload: {check_payload(msg, actual_session.payload, types)}") # for now print but later raise error
                            await send_queues[actual_session.actor].put(msg)  # queue message for recipient
                            print(f"Message sent by {name} to {actual_session.actor}") # to track what proxy is doing at moment -> could be removed
                        except Exception as e:
                            print(f"to, {e}") # debug
                            return End()
                    case _:
                        return End()
                # update sessions to use in while loop
                actual_session = actual_session.cont
                # actual_sessions = (ses_server_actual.cont, ses_client_actual.cont) # after a single session start next session
            case(Choice()):
                try:
                    # case 1: the actor to whom this session belongs chooses branch
                    if actual_session.actor == name:
                        # 1: receive branch index
                        branch = await recv_queues[name].get() # is received directly from actor!
                        print(f"choice of {name}, chose branch {json.loads(branch)}") # debug
                        # 2: send to involved parties
                        for act in actual_session.actors_involved:
                            if act != name:
                                print(f"sending branch decision from {name} to {act}") # debug
                                await send_queues[act].put(branch)
                    # case 2: this actor RECEIVES a branch index
                    else:
                        branch = await send_queues[name].get()
                        await actor_list[name].send(branch)

                    # for both, set sessions
                    doing.append(actual_session)
                    actual_session = actual_session.alternatives[json.loads(branch)][0] # start with first action, others follow with cont
                    print(f"at {name}, doing {actual_session.label} after choice")
                except Exception as e:
                    print(f"choice, {e}, actor fail:{name}") # debug
                    return End()
            case(Ref()):
                print(f"doing ref {actual_session.name}")
                for item in reversed(doing):
                    if isinstance(item, Rec) and item.label == actual_session.name:
                        actual_session = item # .actions[0]
                        break
                try: 
                    pass
                except Exception as e:
                    print(f"ref problem, {e}") # debug
                    return End()
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
        # if last action in rec or choice, do next session cont of rec/choice and close rec/choice
        if not actual_session: # if actual session is None; a next cont indicates for choice and rec that their list of actions is over and we might close them
            actual_session = doing[-1].cont
            print(f"replacing None ses with {type(doing[-1].cont)} from {type(doing[-1])} for actor {name}") # debug
            doing.pop()
    return End() # only returned when session is end


