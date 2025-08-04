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

 
async def ws_client(port):
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
            time.sleep(3)
            rec = True
            while rec:
                rec = False # will nit repeat unless explicictly stated
                print(f"Consumer is offering {propose}. Accept? Write Yes, No, or Propose: ")
                user_accept = input()
                if user_accept == "Yes": # choose branch 0
                    await ws.send(json.dumps(0))
                    time.sleep(3)
                    await ws.send() # accept
                    confirm = json.loads(await ws.recv())
                elif user_accept == "No": # choose branch 1
                    await ws.send(json.dumps(1))
                    time.sleep(3)
                    await ws.send() # reject
                else: # choose branch 2
                    await ws.send(json.dumps(2))
                    time.sleep(3)
                    await ws.send(json.dumps(11)) # propose
                    choice_two = json.loads(await ws.recv())
                    match choice_two:
                        case 0:
                            accept = json.loads(await ws.recv())
                            print("consumer has said accepted")
                            time.sleep(3)
                            await ws.send() # confirm; can i send without anything?
                        case 1:
                            time.sleep(3)
                            reject = json.loads(await ws.recv())
                        case 2:
                            propose = json.loads(await ws.recv())
                            time.sleep(3)
                            print(f"Consumer has proposed {propose}")
                            rec = True



    except websockets.exceptions.ConnectionClosed:
        print(f"Connection lost, most likely due to a timeout")
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