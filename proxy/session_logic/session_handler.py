from session_types import *
from websockets.legacy.server import WebSocketServerProtocol, serve # for websockets server websocket
from websockets import ClientProtocol # for websockets client
from typing import Any

# proxy has to do the sending and receiving!!

# not used for now
async def send(actor_list, actor:str, message:Any, websocket:ClientProtocol|WebSocketServerProtocol): # message is an Any because we'll send a json
    # function s.d. an actor can send a message to another, because proxy has list of actors<->sockets
    # to will be actor's "nickname" -> have we added that to list? See how to!
    # correct kind of websocket; it should only be one type
    await actor_list[actor].send(message) # -> getting name from list will give back socket
    # but how does function know it's sending from proxy's side????



# suppose async because we're handling messages
async def handle_session(name:str, ses:Session, actor_list) -> End: # does it actually always return End??
    # need proxy socket so we can se the send and receive functions from websockets??
    # we need the actor list so we can relate sockets to actor for the sending and receiving of messages?
    # initialize sessions
    # name is name of actor carrying ses out rn
    actual_session = ses
    doing_rec = None # keep rec while we go through it so we can go back to it's start if we need to do so
    # payload = None # initialize but will change when there is one
    # carry out sessions in a loop (useful for cont)
    while (not isinstance(actual_session, End)):
        # print(payload) # debug
        match (actual_session):
            case (Message()):
                match (actual_session.dir.dir):
                    case ("from"): # receive message from someone else
                        try:
                            msg = await actor_list[actual_session.actor].recv() # proxy receives message from the actor that's supposed to send it; give over the necessary websocket -> I DONT THINK THIS IS HOW IT WORKS!!! DOUBLE CHECK!! MAYBE IT'S SUPPOSED TO BE PROXY SOCKET AS RECV!!
                            # because sometimes sockets act as servers and sometimes as cleints, no? although proxy will ALWAYS act as server, so idk... maybe it's ok?
                            # proxy should check message ok
                            # print(schema_validation.checkPayload(payload, ses_client_actual.payload, ses_server_actual.payload)) # check client paylaod
                            msg = await actor_list[name].send(msg) # NOW weiterleiten message to actual client that should receive it
                            # payload = None # reset payload to none
                            print(f"Message received by {name}, sent by {actual_session.actor}") # to track what proxy is doing at moment -> could be removed
                        except Exception as e:
                            return End()
                    case ("to"): # send message to someone else
                        try:
                            msg = await actor_list[name].send(msg)
                            # print(schema_validation.checkPayload(payload, ses_client_actual.payload, ses_server_actual.payload)) # check client paylaod
                            msg = await actor_list[actual_session.actor].recv()
                            # payload = None # reset payload to none
                            print(f"Message sent by {name}, received by {actual_session.actor}") # to track what proxy is doing at moment -> could be removed
                        except Exception as e:
                            return End()
                    case _:
                        return End()
                # actual_sessions = (ses_server_actual.cont, ses_client_actual.cont) # after a single session start next session
            case(Choice()):
                # how to we go "out" of the choice session with a cont, if we first have to carry out sessions inside -> solution for now:
                #   when a cont session is define, define cont of last action in an alternative as the cont of the choice session
                try:
                    # command with message later
                    """
                    # in case the command has payload with it
                    if not isinstance(command, str): # if it has payload it's of type list with action and payload; if not, it'd just string
                        payload = command[1]
                        print(f"payload type in choice: {type(payload)}") # debugging
                        action = command[0]
                    else:
                        action = command
                    print(f'Carrying out {action} action...') # to track what proxy is doing at moment -> could be removed
                    """
                    # actual_session = actual_session.lookup(Label(action)), ses_client_actual.lookup(Label(action))) # next sessions will be singles
                    actual_session = actual_session.alternatives[0]
                except Exception as e:
                    return End()
                # payload = json.dumps(payload) # pack payload into json again for payload checks and transportation
            case(Rec()):
                doing_rec = actual_session
                try: 
                    pass
                except Exception as e:
                    return End()
            case _:
                return End()
        # update sessions to use in while loop
        actual_session = actual_session.cont
    return End() # only returned when session is end
