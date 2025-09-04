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
            await ws.send(json.dumps("Agency"))
            await ws.recv() # will get when all actors join
            
            print(f"All actors have joined. Initializing programm...")
            
            cities = ["Paris", "London", "New York", "Berlin"]
            prices = ["700", "500", "650", "451"]

            while True:
                c_choice = json.loads(await ws.recv())
                if c_choice == "query":
                    query = json.loads(await ws.recv())
                    maybe_error = json.loads(await ws.recv()) # receive from proxy itself
                    if "Schema validation error at query" in maybe_error[0]: # TODO: should i check in most recent error or not really?
                        print("The payload type was wrong! Customer will try again...")
                        # to C
                        await ws.send(json.dumps("wrongPayload"))
                        await ws.send(json.dumps(None))
                        # to S
                        await ws.send(json.dumps("wrongPayload"))
                        await ws.send(json.dumps(None))
                    else:
                        print(f"Customer is asking for {query}")
                        await ws.send(json.dumps("price"))
                        await ws.send(json.dumps(800)) # send price to C; TODO: adjust to make sense
                        await ws.send(json.dumps("info"))
                        await ws.send(json.dumps("Sending info to C...")) # send info to S
                    # from here back to loop
                elif c_choice == "ACCEPT":
                   print("Customer has accepted the trip")
                   accept = json.loads(await ws.recv())
                   await ws.send(json.dumps("ACCEPT"))
                   await ws.send(json.dumps(None))
                elif c_choice == "REJECT":
                   print("Customer has rejected the trip")
                   reject = json.loads(await ws.recv())
                   await ws.send(json.dumps("REJECT"))
                   await ws.send(json.dumps(None))
                elif c_choice == "error":
                   error = json.loads(await ws.recv())
                   print(f"Error in program: {error}. Trying again...")
                   await ws.send(json.dumps("error"))
                   await ws.send(json.dumps(error))


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