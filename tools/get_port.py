import socket

def get_free_port() -> int:
    '''
    Checks which ports are available for a proxy to use.

        Returns:
            The number of the free protocol.
    '''
    # opens a free port randomly and registers its name so we can know which one it is
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0)) # “0” means “give me any free port”
    port = s.getsockname()[1]
    s.close()
    return port

if __name__ == "__main__":
    print(get_free_port())