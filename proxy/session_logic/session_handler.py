import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from session_types import *
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
async def handle_session(name:str, ses:Session, actor_list, recv_queues) -> End: # does it actually always return End??
    # need proxy socket so we can se the send and receive functions from websockets??
    # we need the actor list so we can relate sockets to actor for the sending and receiving of messages?
    # initialize sessions
    # name is name of actor carrying ses out rn
    actual_session = ses
    print(f"in handler, {actual_session}") # debug
    doing:list[Session] = [] # actually restrict sessions inside to only be choice or rec
    
    # functions to tack where we are in a rec or choice session
    # rec_and_choice:list[(Session, int, int)] = None # (Session, index(which action we are in), index of last action )
    # idea: for rec, have something opened and when cont = None, close and go to Rec's cont

    # payload = None # initialize but will change when there is one
    # carry out sessions in a loop (useful for cont)
    
    print(f"carrying out ses {actual_session} for {name}")
    while (not isinstance(actual_session, End)):
        # print(payload) # debug
        match (actual_session):
            case (Message()):
                match (actual_session.dir.dir):
                    case ("from"): # receive message from someone else
                        try:
                            msg = await recv_queues[actual_session.actor].get() # proxy receives message from the actor that's supposed to send it; give over the necessary websocket -> I DONT THINK THIS IS HOW IT WORKS!!! DOUBLE CHECK!! MAYBE IT'S SUPPOSED TO BE PROXY SOCKET AS RECV!!
                            # because sometimes sockets act as servers and sometimes as cleints, no? although proxy will ALWAYS act as server, so idk... maybe it's ok?
                            # proxy should check message ok
                            # print(schema_validation.checkPayload(payload, ses_client_actual.payload, ses_server_actual.payload)) # check client paylaod
                            await actor_list[name].send(msg) # NOW weiterleiten message to actual client that should receive it
                            # payload = None # reset payload to none
                            print(f"Message received by {name}, sent by {actual_session.actor}") # to track what proxy is doing at moment -> could be removed
                        except Exception as e:
                            print(f"from, {e}") # debug
                            return End()
                    case ("to"): # send message to someone else
                        try:
                            msg = await recv_queues[name].get()
                            # print(schema_validation.checkPayload(payload, ses_client_actual.payload, ses_server_actual.payload)) # check client paylaod
                            await actor_list[actual_session.actor].send(msg)
                            # payload = None # reset payload to none
                            print(f"Message sent by {name}, received by {actual_session.actor}") # to track what proxy is doing at moment -> could be removed
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
                    # give int 0 - ? to indicate which choice branch to take. Might change that later!
                    # will receive int with indication of chosen option; doesn't matter if current actor or others, it's the same for the list
                    
                    print(f"ses: {actual_session}, actor to/from: {actual_session.actor} in {name}")
                    branch = await recv_queues[actual_session.actor].get()
                    # let involved parties know which branch will be taken
                    print(f"is actors involved ok? : {actual_session.actors_involved}") # debug
                    for act in actual_session.actors_involved:
                        print(f"sending branch decision to {act} on {actor_list[act]}") # debug
                        await actor_list[act].send(branch)
                    print(f"branch type {type(branch)}")
                    print(f"{name} taking branch {branch}")
                    doing.append(actual_session)
                    actual_session = actual_session.alternatives[json.loads(branch)][0] # start with first action, others follow with cont
                    print(f"at {name}, doing {actual_session.label} after choice")
                except Exception as e:
                    print(f"choice, {e}, actor fail:{name}") # debug
                    return End()
            case(Ref()):
                for item in reversed(doing):
                    if isinstance(item, Rec) and item.label == actual_session.name:
                        actual_session = item # .actions[0]
                        break
                try: 
                    pass
                except Exception as e:
                    print(f"ref, {e}") # debug
                    return End()
            case(Rec()):
                # declare rec and go inside rec list to do actions
                doing.append(actual_session)
                actual_session = doing[-1].actions[0]
                try: 
                    pass
                except Exception as e:
                    print(f"rec, {e}") # debug
                    return End()
            # case _:
                # return End()
            #debug
            case _other:
                # unexpected node type — log it and break the loop
                print(f"Unhandled session node: {actual_session.kind} {actual_session.label}")
        # if last action in rec or choice, do next session cont of rec/choice and close rec/choice
        if not actual_session: # if actual session is None; a next cont indicates for choice and rec that their list of actions is over and we might close them
            actual_session = doing[-1].cont
            doing.pop()
    return End() # only returned when session is end


