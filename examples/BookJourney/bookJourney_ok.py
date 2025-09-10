import requests
import asyncio
import subprocess, sys, os

project_root = os.path.dirname(os.path.abspath(__file__))

base_url = 'http://127.0.0.1:8000/'

async def send_requests():

    try:

        # send protocol
        protocol = '''{
            "protocol": "BookJourney",
            "roles": [
                { "name":"Agency", "alias":"A" },
                { "name":"Service", "alias":"S" },
                { "name":"Customer", "alias":"C" }
            ],
            "error": "handle",
            "timeout": 60.0,
            "body": [
                {
                "kind":"rec", "label":"LOOP", "body":[
                    {
                    "kind":"choice","at":"C","options":[
                        [ { "kind":"message","name":"query","from":"C","to":"A","payload":"str" },
                            {
                            "kind":"choice","at":"A","options":[
                            [ { "kind":"message","name":"wrongPayload","from":"A","to":"C","payload":"" },
                            { "kind":"message","name":"wrongPayload","from":"A","to":"S","payload":"" },
                                { "kind":"continue","label":"LOOP"} ],
                            [ { "kind":"message","name":"price","from":"A","to":"C","payload":"int" },
                                { "kind":"message","name":"info","from":"A","to":"S","payload":"str" },
                                { "kind":"continue","label":"LOOP" } ]
                            ]
                        }
                        ],
                        [ { "kind":"message","name":"ACCEPT","from":"C","to":"A","payload":"" },
                        { "kind":"message","name":"ACCEPT","from":"A","to":"S","payload":"" },
                        { "kind":"message","name":"Address","from":"C","to":"S","payload":"str" } ],
                        [ { "kind":"message","name":"REJECT","from":"C","to":"A","payload":"" },
                        { "kind":"message","name":"REJECT","from":"A","to":"S","payload":"" } ],
                            [ { "kind":"message","name":"timeout","from":"C","to":"A","payload":"str" },
                            { "kind":"message","name":"timeout","from":"A","to":"S","payload":"str" },
                            { "kind":"continue","label":"LOOP" } ]
                        ]
                        }
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

    # run customer actor code
    subprocess.Popen(
        [sys.executable, "-m", "customer_ok", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

    # run Buyer actor code
    subprocess.Popen(
        [sys.executable, "-m", "service", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

    # run Seller actor code
    subprocess.Popen(
        [sys.executable, "-m", "agency", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

