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
            await ws.send(json.dumps("Authenticator"))
            await ws.recv() # will get when all actors join
            
            print(f"All actors have joined. Initializing programm...")

            users = ["barista", "owner", "customer", "guest"]
            
            while True: # might have to change
                login = json.loads(await ws.recv())
                if login not in users:
                    await ws.send(json.dumps(False))
                    await ws.send(json.dumps(False)) # actually will have to reduce to one step later
                else:
                    await ws.send(json.dumps(True))
                    await ws.send(json.dumps(True)) # actually will have to reduce to one step later


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