# multiparty-proxy
A proxy for multiparty session-typed communication

## prerequistes:
* python 3
* windows computer (some functionalities might work in other opertating systems but it hasn't been tried)
* the following python libraries:
    * uvicorn
    * fastAPI
    * websockets
    
* not required but : have your python be executable from the command prompt when carrying out the "python" command

## sending requests
1) start the API by executing the start_api.bat file or carrying out the command: "python -m uvicorn API.meetingAPI:app --reload" from the project directory
2) to send requests, follow the specification as described in the document* along with your preferred method to send API requests (base URL: http://127.0.0.1:8000/), or go to "" in your browser
   to see a thorough explanation of the endpoints and send the requests from there.
3) once a meeting is defined through the request, the port of the proxy the clients operating with a websockets client protocol is given.

## where information is
* the global Scribble protocol in a .scr file will be under API/[protocol_name]
* the local Scribble protocols will be under proxy/[protocol_name]
* the logging file with ddebugging outputs will be in proxy/[protocol_name] and will have the format [port_number]_log.txt


## running examples

### Negotiate

1) For a correct usage:
  a) run the negotiate_ok.py script and follow the instructions in the oepened customer and producer SOEMTHING or
  b) Send API requests to define the "contact" custom type and then the Negotitate protocol as specified in the negotiate_ok.py file, then run the customer.py and producer.py files with the port
     number that was given as response to the POST meeting request. For example:
     python -m producer -p [port_number]

2) To see how a fatal timeout error is carried out:

### Purchase

## BookJourney

