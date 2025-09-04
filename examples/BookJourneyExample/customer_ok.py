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
            await ws.send(json.dumps("Customer"))
            await ws.recv() # will get when all actors join
            
            print(f"All actors have joined. Initializing programm...")

            while True:
                possible_errors = json.loads(await ws.recv()) # check if any errors
                if not possible_errors: # if error list is empty
                    choice = input("Accept or reject last offer? Or ask for a city? Write 'ask' or 'accept' or 'reject': ").lower()
                    if choice == "ask":
                        city = input("Ask for city (Paris, London, New York or Berin): ")
                        await ws.send(json.dumps("query"))
                        await ws.send(json.dumps(city))

                        choice_a = json.loads(await ws.recv())
                        if choice_a == "wrongPayload":
                            wrong_payload_message = json.loads(await ws.recv())
                            print("Something went wrong. Trying again...")
                        elif choice_a == "price":
                            price = json.loads(await ws.recv())
                            print(f"The price for the trip would be {price} euros")
                    else:
                        ignore_errors = json.loads(await ws.recv()) # will receive a series of errors but we decided not to hnalde those
                        if choice == "accept":
                            await ws.send(json.dumps("ACCEPT"))
                            await ws.send(json.dumps(None))
                            address = input("Please write your address in order to book your trip: ")
                            await ws.send(json.dumps("Address"))
                            await ws.send(json.dumps(address))
                            print("Information has been sent. See you later!")
                        elif choice == "reject":
                            print("Offer has been rejected. See you soon!")
                            await ws.send(json.dumps("REJECT"))
                else:
                    await ws.send(json.dumps("error"))
                    print(f"Error in program: {possible_errors[0]}. Trying again...")



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