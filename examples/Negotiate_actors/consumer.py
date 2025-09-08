# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# for sending/receiving with proxy + proxy error exceptions
#from session_logic.helpers import *

import websockets
import asyncio
import time # to keep console opened for a bit after code is finished
import json
import argparse

async def ws_client(port:int):
    '''
    Handles connection and sends and receives payloads according to interaCtion with user.
    '''
    try:
        print("Connecting client...")
        url = f"ws://127.0.0.1:{port}" # 7891 is proxy port

        # Connect to the proxy/server
        async with websockets.connect(url) as ws:
            await ws.send(json.dumps("Consumer"))
            await ws.recv() # will get when all actors join
            print(f"All actors have joined. Initializing programm...")
            
            prop = input("Write a number to propose: ")
            
            await ws.send(json.dumps("propose"))
            await ws.send(json.dumps(int(prop)))
            # await asyncio.sleep(3)
            rec = True
            while rec:
                rec = False # will nit repeat unless explicictly stated
                choice_one = json.loads(await ws.recv())
                match choice_one:
                    case "accept":
                        json.loads(await ws.recv()) # accept
                        print("producer has said accepted")
                        p_contact = json.loads(await ws.recv())
                        print(f"Producer's name: {p_contact['name']}")
                        print(f"Producer's email: {p_contact['email']}")
                        # await asyncio.sleep(3)
                        await ws.send(json.dumps("confirm"))
                        await ws.send(json.dumps(None)) 
                    case "reject":
                        json.loads( await ws.recv()) # reject
                    case "propose":
                        propose = json.loads(await ws.recv()) # int
                        print(f"Producer is offering {propose}. Accept? Write Yes, No, or Propose: ")
                        user_accept = input()
                        if user_accept == "Yes": # choose branch 0
                            await ws.send(json.dumps(0))
                            # await asyncio.sleep(3)
                            await ws.send(json.dumps(None)) # accept
                            json.loads(await ws.recv()) # confirm
                        elif user_accept == "No": # choose branch 1
                            await ws.send(json.dumps(1))
                            # await asyncio.sleep(3)
                            await ws.send(json.dumps(None)) # reject
                        else: # choose branch 2
                            await ws.send(json.dumps(2))
                            # await asyncio.sleep(3)
                            prop = input("Write a number to propose: ")
                            await ws.send(json.dumps(int(prop)))# propose
                            rec = True # continue X
                    case _:
                        print("Invalid choice from another actor.")
                        raise

    except websockets.exceptions.ConnectionClosed:
        print(f"Connection lost")
    #except ProxyError as e:
        #print(e)
    except Exception as e:
        print(f"Unexpected error {e}")
    finally:
        print("Closing client in 5 seconds...")
        time.sleep(5)
        exit()

#-- Start the client code ------------------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default="7891", help="Proxy port number")
    args = parser.parse_args()
    asyncio.run(ws_client(args.port))