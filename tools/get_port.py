import socket

def get_free_port() -> int:
    """Ask the OS for an unused port by binding to port 0."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))           # “0” means “give me any free port”
    port = s.getsockname()[1]
    s.close()
    return port

if __name__ == "__main__":
    print(get_free_port())