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

        # dicts for product info
        products_available = {}
        products_available["coffee"] = 10
        products_available["tea"] = 25
        products_available["sugar"] = 100
        products_available["cup"] = 4

        products_prices = {}
        products_prices["coffee"] = 30.15
        products_prices["tea"] = 22.00
        products_prices["sugar"] = 5.42
        products_prices["cup"] = 56.75

        products_shops = {}
        products_available["coffee"] = ["Park", "Coffee Shop", "Supermarket"]
        products_available["tea"] = ["Park", "Coffee Shop", "Supermarket"]
        products_available["sugar"] = ["Supermarket"]
        products_available["cup"] = ["Coffee Shop", "Supermarket"]


        # Connect to the proxy/server
        async with websockets.connect(url) as ws:
            await ws.send(json.dumps("Seller"))
            await ws.recv() # will get when all actors join
            
            print(f"All actors have joined. Initializing programm...")
            
            login = await ws.recv()
            await ws.send(login) # send to Authenticator, already in JSON
            auth = json.loads(await ws.recv())
            match auth:
                case True:
                    print("The user has been authenticated")
                case False:
                    print("The user has not been authenticated. Proceed with caution.")
            choice_b = json.loads(await ws.recv())
            match choice_b:
                case 0:
                    req = json.loads(await ws.recv())
                    print(f"Checking price of product: {req}")
                    price = products_prices[req]
                    await ws.send(json.dumps(price))
                    print(f"The product costs {price} per unit.")
                case 1:
                    product = json.loads(await ws.recv())
                    print(f"Buying {product} ...")
                    products_available[product] =- 1 
                    location = products_shops[product][0]
                    print(f"Send product to {location}")
                    await ws.send(json.dumps(location))
                case 2:
                    await ws.recv()


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