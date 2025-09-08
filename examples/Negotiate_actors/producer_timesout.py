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
    Handles connection and sends and receives payloads according to interaction with user.
    '''
    try:
        print("Connecting client...")
        url = f"ws://127.0.0.1:{port}" # 7891 is proxy port

        # Connect to the proxy/server
        async with websockets.connect(url) as ws:
            await ws.send(json.dumps("Producer"))
            await ws.recv() # will get when all actors join
            
            print(f"All actors have joined. Initializing programm...")
            
            propose = json.loads(await ws.recv())
            # await asyncio.sleep(3)
            rec = True
            while rec:
                rec = False # will not repeat unless explicictly stated
                print(f"Consumer is offering {propose}. Accept? Write Yes, No, or Propose: ")
                user_accept = input()
                if user_accept == "Yes": # choose branch 0
                    # await asyncio.sleep(3)
                    await ws.send(json.dumps("accept"))
                    await ws.send(json.dumps(None)) # accept
                    await asyncio.sleep(40)
                    contact = {
                            "name":  "Alice",
                            "email": "alice@gmail.com"
                        }
                    await ws.send(json.dumps("contact"))
                    await ws.send(json.dumps(contact))
                    json.loads(await ws.recv()) # confirm
                elif user_accept == "No": # choose branch 1
                    # await asyncio.sleep(3)
                    await ws.send(json.dumps("reject"))
                    await ws.send(json.dumps(None)) # reject
                else: # choose branch 2
                    await ws.send(json.dumps(2))
                    # await asyncio.sleep(3)
                    prop = input("Write a number to propose: ")
                    await ws.send(json.dumps("propose"))
                    await ws.send(json.dumps(int(prop)))# propose
                    choice_two = json.loads(await ws.recv())
                    match choice_two:
                        case "accept":
                            json.loads(await ws.recv()) # accept
                            print("consumer has said accepted")
                            await ws.send(json.dumps("confirm"))
                            await ws.send(json.dumps(None))
                        case "reject":
                            json.loads(await ws.recv()) # reject
                        case "propose":
                            propose = json.loads(await ws.recv())
                            rec = True
                        case _:
                            print("Another actor chose wrong option.")
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