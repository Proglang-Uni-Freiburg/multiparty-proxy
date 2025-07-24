import argparse
import asyncio
import websockets
from websockets.legacy.server import WebSocketServerProtocol, serve # for websockets server
from websockets.legacy.client import WebSocketClientProtocol # for websockets client
import json

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from scribble_python.wf_checker import project_protocol

def project_actors(actors:list[str], protocol_name: str):
    for a in actors:
        project_protocol(
        scr_path=f"API/protocols/{protocol_name}.scr",
        full_global=f"{protocol_name}.{protocol_name}", # for now because protocol + module but maybe change later
        role=a,
        output_dir=f"proxy/protocols/{protocol_name}/{a}.scr"
    )

async def actor_handler(clientSocket: WebSocketServerProtocol, path, actor_slots, protocol_info, all_connected_evt: asyncio.Event):
    """
    Add description
    """
    try:
        actor_name = await clientSocket.recv()
        if actor_name not in actor_slots:
            await clientSocket.send(json.dumps("This actor does not exist in this meeting."))
            return await clientSocket.close()
        actor_slots[actor_name] = clientSocket
        print(f"{actor_name} joined the meeting.")
        await clientSocket.send(json.dumps("500: Operation succesful."))# send ok code
        
        # fire the event if we’re complete
        if all(actor_slots[a] for a in actor_slots):
            all_connected_evt.set()

        # wait for everybody
        await all_connected_evt.wait()

        await clientSocket.send(json.dumps("502: All actors have joined session."))

        # while True:
            # await clientSocket.recv() # temporary
        
        # accept actions and handle them
        while True:
            try:
                actionName = await clientSocket.recv()
                # await handle_session(Ref(actor_name), clientSocket, actor_slots, protocol_info, actionName) # def session + action name
            except websockets.ConnectionClosed:
                break

    except websockets.ConnectionClosed:
        pass
    finally:
        # cleanup
        if actor_slots.get(actor_name) is clientSocket:
            actor_slots[actor_name] = None
            print(f"Actor {actor_name} disconnected")

async def main_proxy(proxy_port: int, actors_complete, protocol_name: str):
    print(f"Starting proxy for protocol {protocol_name} in port {proxy_port}...")
    actors = [name for name, alias in actors_complete]
    project_actors(actors, protocol_name) # make necessary projections
    actor_slots = {actor: False for actor in actors} # initialize connections list
    
    all_joined_evt = asyncio.Event()
    protocol_info = None # temp

    # wait for actors to join
    print("Waiting for all actors to join...")
    async with serve(
        lambda ws, path: actor_handler(ws, path, actor_slots, protocol_info, all_joined_evt),
        "localhost",
        proxy_port
    ):
        # once all actors are joined
        await all_joined_evt.wait()
        print("All actors connected. Starting the meeting...")
        await asyncio.Future() # so that server doesn't close
