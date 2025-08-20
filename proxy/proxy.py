# websockets imports
import websockets
from websockets.legacy.server import WebSocketServerProtocol, serve # for websockets server
from websockets.legacy.client import WebSocketClientProtocol # for websockets client # TODO: see if we use this

# to be able to use modules from other files in the project
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# imports from other files in project
from scribble_python.wf_checker import project_protocol
from proxy.session_logic.session_handler import *
from proxy.session_logic.session_parsers import *
from proxy.session_logic.type_validation import *

# other imports
import json
import asyncio # for creating asynchronous tasks, events, queues, etc.
import httpx # for sending API requests
import shutil # to erase scr files of protocol once meeting is done

# -- queues for sending/receiving messages in sessions ------------------------------------------------------------------
async def receiving_queue(actor: str, ws,
                      queue: asyncio.Queue[str]):
    '''
    Creates and enables access to a queue where all messages received from an actor through their websocket are stored.

        Args:
            actor(str): name of the session actor #TODO: what was formal name of actor in Scribble?
            ws(): websocket linked with said actor
            queue: queue object with which messages are stored and received
    '''
    try:
        async for msg in ws: # does ws.recv() and extracts message from it
            await queue.put(msg)
    except Exception as e:
        print(f"Problem with receiving queue for {actor}: {e}") # TODO: raise instead of print

async def sending_queue(actor: str, ws,
                      queue: asyncio.Queue[str]):
    '''
    Creates and enables access to a queue where all messages to be sent to the actor are stored.

    WARNING: They are however not sent; we properly send them in the session handler.

        Args:
            actor(str): name of the session actor #TODO: what was formal name of actor in Scribble?
            ws(): websocket linked with said actor
            queue: queue object with which messages are stored
    '''
    try:
        while True:
            msg = await queue.get()
    except Exception as e:
        print(f"Problem with sending queue for {actor}: {e}") # TODO: raise instead of print


# -- actor logic for a meeting -------------------------------------------------------------------------------------------
def project_actors(actors:list[str], protocol_name: str):
    '''
    Creates a series of scr files in the protocols folder in the proxy that contains a Scribble projected local protocol for each
    of the actors in a meeting. 

        Args:
            actors(list[str]): list of names of actors in protocol
            protocol_name(name): name of protocol (aka meeting) so we can locate its scr in the API folder
    '''
    for a in actors:
        project_protocol(
        scr_path=f"API/protocols/{protocol_name}.scr",
        full_global=f"{protocol_name}.{protocol_name}",
        role=a,
        output_dir=f"proxy/protocols/{protocol_name}"
    )

async def actor_handler(clientSocket: WebSocketServerProtocol, path, actor_slots:dict, actors_complete, protocol_name:str, incoming_queues, outgoing_queues, types, all_connected_evt: asyncio.Event, all_done_evt: asyncio.Event):
    '''
    When a socket connects to proxy, check if they want to connect as an actor in the meeting, then initialize and handle a session for said actor.

        Args:
            clientSocket(): actor socket that is connected to the proxy
            path(): needed to use proxy in "serve" mode
            actor_slots(dict): dict with whcih one can find the websockets port assigned to an actor (actor: port)
            actors_complete(): list of all actors along with their aliases (the shortened version of their names that is used in the projected Scribble protocol)
            protocol_name(str): name of the protocol (aka meeting) the proxy is regulating
            incoming_queues(): find a receiving queue of an actor by looking up their alias (alias: queue)
            outgoing_queues(): find a receiving queue of an actor by looking up their alias (alias: queue)
            types: JSON schemas of all the types, referenced by the name of the type
            all_connected(): event that lets handler know when all actors have joined the meeting and the sessions can start
    '''
    # declare an actor and wait for others to join
    try:
        # register actor
        actor_name = json.loads(await clientSocket.recv())
        if actor_name not in actor_slots:
            print(f"{actor_name} not found") # debug
            await clientSocket.send(json.dumps("This actor does not exist in this meeting."))
            return await clientSocket.close()
        actor_slots[actor_name] = clientSocket
        print(f"In meeting {protocol_name}: {actor_name} joined the meeting.") # debug
        
        # create session based on protocol
        actor_ses = scr_into_session(f"proxy/protocols/{protocol_name}/{protocol_name}_{protocol_name}_{actor_name}.scr")

        # make receiving queue
        actor_alias = next(alias for name, alias in actors_complete if name == actor_name) # TODO: maybe declare aliases at start or even before the handler, in main
        recv_task = asyncio.create_task(receiving_queue(actor_alias, clientSocket, incoming_queues[actor_alias])) # so that the receiving queue can use the websockets recv function

        # fire the event if all actors have joined
        if all(actor_slots[a] for a in actor_slots):
            all_connected_evt.set()
        # wait for everybody
        await all_connected_evt.wait()
        await clientSocket.send(json.dumps("502: All actors have joined session.")) # TODO: change depending on error definitions

        # start tracking session
        # first, make actor - socket list actually be a list of ALIASES - socket because protocol tracks aliases -> should probaly do in main proxy instead of actor handler
        alias_slots = {alias: actor_slots[name] for name, alias in actors_complete} # TODO: change this maybe, see above
        ending = await handle_session(actor_alias, actor_ses, alias_slots, incoming_queues, outgoing_queues, types) # def session + action name
        if ending == End():
            # mark as finished and check if all finished
            if actor_slots.get(actor_name) is clientSocket:
                actor_slots[actor_name] = None
            if all(actors is None for actors in actor_slots.values()): # if all other actors have disconnected
                all_done_evt.set() # fire event to close proxy
            await all_done_evt.wait()
            # close gracefully
            await clientSocket.close(code=1000, reason="Session ended successfully")
            await clientSocket.wait_closed()
            print(f"{actor_name}'s session is finished and the actor has been disconnected from the session.")
            recv_task.cancel() # close receiving queue task
            return
    
    # handle ok disconnections
    except (websockets.ConnectionClosed, websockets.ConnectionClosedError, websockets.ConnectionClosedOK): # TODO: fix ConenctionClosed positional arguments
        print(f"An error has been encountered in {actor_name} and its connection was closed.")
    except (SchemaValidationError) as e: # TODO: raise inside handler
        print(f"Type mismatch {e} in {actor_name}. Actor dsiconnected.")
    # except TimeoutError as e: # TODO: implement later
        # print(f"{e}")
    except Exception as e:
        print(f"Unexpected error in proxy: {e}")
    finally:
        pass

# -- initialize ------------------------------------------------------------------------------------------------------------------------------------
async def main_proxy(proxy_port:int, actors_complete, protocol_name: str, types):
    '''
    Opens proxy for a meeting and calls functions to connect actors and handle their sessions.

        Args:
            proxy_port(int): number of the port the proxy is serving from
            actors_complete(): __ of actors and their aliases
            protocol_name(str): Name of protocol (meeting)
            types(): all payload types that will come up in the meeting along with their JSON schemas
    '''
    #TODO: do try and clean up maybe
    print(f"Starting proxy for protocol {protocol_name} in port {proxy_port}...")
    actors = [name for name, alias in actors_complete]
    project_actors(actors, protocol_name) # make necessary projections
    actor_slots = {actor: None for actor in actors} # initialize connections list
    aliases = [alias for _n,alias in actors_complete]
    incoming_queues = { alias: asyncio.Queue() for alias in aliases } # from actor
    outgoing_queues = { alias: asyncio.Queue() for alias in aliases } # to actor
    
    all_joined_evt = asyncio.Event() # will be fired when all actors have joined
    all_done_evt   = asyncio.Event() # will be fired when all actors are disconnected

    # wait for actors to join
    print(f"In meeting {protocol_name}: waiting for all actors to join...") # debug
    async with serve(
        lambda ws, path: actor_handler(ws, path, actor_slots, actors_complete, protocol_name, incoming_queues, outgoing_queues, types, all_joined_evt, all_done_evt),
        "localhost",
        proxy_port
    ):
        try: 
            # once all actors are joined
            await all_joined_evt.wait()
            print("All actors connected. Starting the meeting...")
            # await asyncio.Future() # so that server doesn't close
            # close proxy gracefullly
            await all_done_evt.wait() # close proxy once all actors are disconnected
            print("All actors have disconnected from the meeting. Deleting meeting and shutting down proxy...")
            await asyncio.sleep(5) # for debug purposes
            # erase protocol from folder
            shutil.rmtree(f"proxy/protocols/{protocol_name}", ignore_errors=False, onerror=None)
            # close meeting properly by sending a delete request to the API
            async with httpx.AsyncClient() as client:
                resp = await client.delete(f"http://localhost:8000/meetings/{protocol_name}")
                if resp.status_code == 204:
                    print(f"Successfully deleted meeting {protocol_name} from API")
                else:
                    print(f"Failed to delete meeting {protocol_name}: {resp.status_code} {resp.text}")
            print("Stopped serving") # debug
            return
        except Exception as e:
            print(f"proxy exception: {e}")