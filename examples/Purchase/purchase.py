import requests
import asyncio
import subprocess, sys, os

project_root = os.path.dirname(os.path.abspath(__file__))

base_url = 'http://127.0.0.1:8000/'

async def send_requests():

    try:

        # send protocol
        protocol = '''{
            "protocol": "Purchase",
            "roles": [
                { "name":"Buyer", "alias":"B" },
                { "name":"Seller", "alias":"S" },
                { "name":"Authenticator", "alias":"A" }
            ],
            "body": [
                { "kind":"message",  "name":"login", "from":"B","to":"S","payload":"str" },
                { "kind":"message",  "name":"login", "from":"S","to":"A","payload":"str" },
                { "kind":"message",  "name":"auth", "from":"A","to":"S","payload":"bool" },
                { "kind":"message",  "name":"auth", "from":"A","to":"B","payload":"bool" },
                {
                "kind":"choice","at":"B","options":[
                        [ { "kind":"message","name":"req","from":"B","to":"S","payload":"str" },
                        { "kind":"message","name":"price","from":"S","to":"B","payload":"float" } ],
                        [ { "kind":"message","name":"buy","from":"B","to":"S","payload":"str" },
                        { "kind":"message","name":"deliver","from":"S","to":"B","payload":"str" } ],
                        [ { "kind":"message","name":"quit","from":"B","to":"S","payload":"" }]
                ]
                }
            ]
            }
        '''
        response = requests.post(base_url+"meetings", data=protocol)
        if response.status_code != 200:
            print(f"Got error when declaring protocol: {response.status_code}")
            raise requests.exceptions.RequestException()
        else:
            print("Declared protocol succesfully...")
            return response.json() # port as int

    except Exception as e:
        print(f"Something went wrong: {e}")
        print("Closing program...")
        await asyncio.sleep(3)


if __name__ == "__main__":
    # send requests
    port = asyncio.run(send_requests())

    # run authenticator actor code
    subprocess.Popen(
        [sys.executable, "-m", "Authenticator", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

    # run Buyer actor code
    subprocess.Popen(
        [sys.executable, "-m", "Buyer", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

    # run Seller actor code
    subprocess.Popen(
        [sys.executable, "-m", "Seller", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

