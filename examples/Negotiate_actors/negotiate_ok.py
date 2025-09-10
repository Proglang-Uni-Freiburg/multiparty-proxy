import requests
import asyncio
import subprocess, sys, os

project_root = os.path.dirname(os.path.abspath(__file__))

base_url = 'http://127.0.0.1:8000/'

async def send_requests():

    try:
        # send custom type schema
        schema = '''{
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title":   "contact",
        "type":    "object",
        "properties": {
        "name":  { "type": "string" },
        "email": { "type": "string", "format": "email" }
        },
        "required": ["name","email"]
        }
        '''
        response = requests.post(base_url+"types/Negotiate/", data=schema)
        if response.status_code != 200:
            print("Couldn't send type")
            raise requests.exceptions.RequestException()
        else:
            print("Declared type succesfully...")

        # send custom type schema
        protocol = '''{
            "protocol": "Negotiate",
            "roles": [
                { "name":"Consumer", "alias":"C" },
                { "name":"Producer", "alias":"P" }
            ],
            "body": [
                { "kind":"message",  "name":"propose", "from":"C","to":"P","payload":"int" },
                {
                "kind":"rec", "label":"X", "body":[
                    {
                    "kind":"choice","at":"P","options":[
                        [ { "kind":"message","name":"accept","from":"P","to":"C","payload":"" },
                                    { "kind":"message","name":"contact","from":"P","to":"C","payload":"contact" },
                        { "kind":"message","name":"confirm","from":"C","to":"P","payload":"" } ],
                        [ { "kind":"message","name":"reject","from":"P","to":"C","payload":"" } ],
                        [ { "kind":"message","name":"propose","from":"P","to":"C","payload":"int" },
                        {
                            "kind":"choice","at":"C","options":[
                            [ { "kind":"message","name":"accept","from":"C","to":"P","payload":"" },
                                { "kind":"message","name":"confirm","from":"P","to":"C","payload":"" } ],
                            [ { "kind":"message","name":"reject","from":"C","to":"P","payload":"" } ],
                            [ { "kind":"message","name":"propose","from":"C","to":"P","payload":"int" },
                                { "kind":"continue","label":"X" } ]
                            ]
                        }
                        ]
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

    # run producer actor code
    subprocess.Popen(
        [sys.executable, "-m", "producer", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

    # run consumer actor code
    subprocess.Popen(
        [sys.executable, "-m", "consumer", "-p", str(port)],
        cwd=project_root,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

