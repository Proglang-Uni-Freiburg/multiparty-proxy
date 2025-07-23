import argparse

if __name__ == "__main__":
    # while True:
    # protocol_info: dict[str, Def] = {} # initialize dictionary for protocols

    # define ports for proxy and server as flags
    parser = argparse.ArgumentParser()
    parser.add_argument("-pr", "--proxyport", default = "7891", help="Proxy port number")
    # parser.add_argument("-s", "--serverport", default = "7890", help="Server port number")
    args = parser.parse_args()
    print(f"Welcome to the proxy!\nProxy port: {args.proxyport}")

    try:
        asyncio.run(main_proxy(int(args.proxyport), protocol_info))
    except Exception as e:
        print("Error in main_proxy:", repr(e))
        raise
