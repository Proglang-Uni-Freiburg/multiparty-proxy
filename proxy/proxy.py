import argparse
import asyncio
import websockets
from websockets.legacy.server import WebSocketServerProtocol, serve # for websockets server
from websockets.legacy.client import WebSocketClientProtocol # for websockets client
import json
from typing import Any

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from scribble_python.wf_checker import project_protocol

from proxy.session_logic.session_handler import *
from proxy.session_logic.session_parsers import *
from proxy.session_logic.type_validation import *

def project_actors(actors:list[str], protocol_name: str):
    for a in actors:
        project_protocol(
        scr_path=f"API/protocols/{protocol_name}.scr",
        full_global=f"{protocol_name}.{protocol_name}", # for now because protocol + module but maybe change later
        role=a,
        output_dir=f"proxy/protocols/{protocol_name}"
    )

"""
def make_session(actor:str, protocol:str):
    # 1. parse projected protocol of actor to a session
    # projected_scr_into_session(actor)) # from session_parsers
        # name of .scr file will be: protocol_name/actor_name.scr/{protocol_name}_{protocol_name}_{actor_name}.scr
        ses = create_session(actor, protocol) # define later
    # 2. go through elements in session
    handle_session(ses:Session, actor_socket:)
"""

async def actor_handler(clientSocket: WebSocketServerProtocol, path, actor_slots, actors_complete, protocol_name, incoming_queues, outgoing_queues, types, all_connected_evt: asyncio.Event):
    """
    Add description
    """
    # stage 1 declare, wait for actors to join
    try:
        # register actor
        actor_name = json.loads(await clientSocket.recv())
        if actor_name not in actor_slots:
            await clientSocket.send(json.dumps("This actor does not exist in this meeting."))
            return await clientSocket.close()
        actor_slots[actor_name] = clientSocket
        print(f"{actor_name} joined the meeting.")
        
        # create session based on protocol
        actor_ses = scr_into_session(f"proxy/protocols/{protocol_name}/{protocol_name}_{protocol_name}_{actor_name}.scr")

        # make receiving queue
        actor_alias = next(alias for name, alias in actors_complete if name == actor_name)

        asyncio.create_task(receiving_queue(actor_alias, clientSocket, incoming_queues[actor_alias]))
        # asyncio.create_task(sending_queue(actor_alias, clientSocket, outgoing_queues[actor_alias]))


        # fire the event if we’re complete
        if all(actor_slots[a] for a in actor_slots):
            all_connected_evt.set()

        # wait for everybody
        await all_connected_evt.wait()

        await clientSocket.send(json.dumps("502: All actors have joined session."))

        # start tracking session
        try:
            # first, make actor - socket list actually be a list of ALIASES - socket because protocol tracks aliases -> should probbaly do in main proxy instead of actor handler
            alias_slots = {alias: actor_slots[name] for name, alias in actors_complete}
            await handle_session(actor_alias, actor_ses, alias_slots, incoming_queues, outgoing_queues, types) # def session + action name
        except websockets.ConnectionClosed:
            print(f"An error has been encountered")

    except websockets.ConnectionClosed:
        pass
    finally:
        # cleanup
        if actor_slots.get(actor_name) is clientSocket:
            actor_slots[actor_name] = None
            print(f"Actor {actor_name} disconnected")

async def receiving_queue(actor: str, ws,
                      queue: asyncio.Queue[str]):
    try:
        async for msg in ws: # maybe rewrite to make it more understandable
            await queue.put(msg)
    except Exception as e:
        print(f"Problem with receiving queue for {actor}: {e}")

async def sending_queue(actor: str, ws,
                      queue: asyncio.Queue[str]):
    try:
        while True:
            msg = await queue.get()
            print(f"{actor} sending {json.loads(msg)} through sending queue") # debug
    except Exception as e:
        print(f"Problem with receiving queue for {actor}: {e}")

async def main_proxy(proxy_port: int, actors_complete, protocol_name: str, types):
    print(f"Starting proxy for protocol {protocol_name} in port {proxy_port}...")
    actors = [name for name, alias in actors_complete]
    project_actors(actors, protocol_name) # make necessary projections
    actor_slots = {actor: None for actor in actors} # initialize connections list
    aliases = [alias for _n,alias in actors_complete]
    incoming_queues = { alias: asyncio.Queue() for alias in aliases } # from actor
    outgoing_queues = { alias: asyncio.Queue() for alias in aliases } # to actor

    
    all_joined_evt = asyncio.Event()

    # wait for actors to join
    print("Waiting for all actors to join...")
    async with serve(
        lambda ws, path: actor_handler(ws, path, actor_slots, actors_complete, protocol_name, incoming_queues, outgoing_queues, types, all_joined_evt),
        "localhost",
        proxy_port
    ):
        # once all actors are joined
        await all_joined_evt.wait()
        print("All actors connected. Starting the meeting...")
        await asyncio.Future() # so that server doesn't close
