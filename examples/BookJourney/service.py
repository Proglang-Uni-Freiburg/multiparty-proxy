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
            await ws.send(json.dumps("Service"))
            await ws.recv() # will get when all actors join
            
            print(f"All actors have joined. Initializing programm...")
            
            while True:
                next = json.loads(await ws.recv())
                print(f"next action = {next}")
                if next == "wrongPayload":
                    json.loads(await ws.recv()) # will receive None, from A
                    print("Error with payload from customer. Trying again...")
                elif next == "info":
                    info = json.loads(await ws.recv()) # from A
                    print(f"Agency says: {info}")
                elif next == "ACCEPT":
                    accept = json.loads(await ws.recv())
                    print("Customer has accepted!")
                    print(f"Acceptance: {accept}")
                    address = json.loads(await ws.recv())
                    print(f"The customer's address is: {address}")
                    break
                elif next == "REJECT":
                    json.loads(await ws.recv()) # reject
                    print("Customer has rejected.")
                    break
                elif next == "timeout":
                    json.loads(await ws.recv())
                    print(f"There was a timeout. Trying again...")

    except websockets.exceptions.ConnectionClosed:
        print(f"Connection lost")
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