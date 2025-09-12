# multiparty-proxy
A proxy for multiparty session-typed communication, based on Scribble protocols. The communication takes place through websockets.

## prerequistes:
* python 3
* windows computer (some functionalities might work in other opertating systems but it hasn't been tried)
* the following python libraries:
    * uvicorn
    * fastAPI
    * websockets
    
* not required but would be very helpful: have your python be executable from the command prompt when carrying out the "python" command.

## sending requests
1) start the API by executing the start_api.bat file or carrying out the command: "python -m uvicorn API.meetingAPI:app --reload" from the project directory
2) to send requests, follow the specification as described in the document* along with your preferred method to send API requests (base URL: http://127.0.0.1:8000/), or go to "http://127.0.0.1:8000/docs" on your browser to see a thorough explanation of the endpoints and send the requests from there.
3) once a meeting is defined through the request, the port of the proxy the clients operating with a websockets client protocol is given.

## where information is
* the global Scribble protocol in a .scr file will be under API/[protocol_name]
* the local Scribble protocols will be under proxy/[protocol_name]
* the logging file with ddebugging outputs will be in proxy/[protocol_name] and will have the format [port_number]_log.txt

## running examples

Note: the examples are very basic, so please write all input exactly as instructed, otherwise code might not work.

In all examples, there are two options:

a) run "python [example.py]", which will automatically send API requests and open a window for each client

b) send the necessary requests yourself and then open the required client python codes with the given port number (e.g. "python -m producer -p [port_number]")

### Negotiate

a) For a correct usage: run the negotiate_ok.py script and follow the instructions in the opened customer and producer windows

b) To see how a fatal timeout error is carried out: run negotiate_timesout.py and wait for timeout

### Purchase

Run purchase.py to try it out.
For username, the options are:
   * barista
   * owner
   * customer
   * guest
For products, the options are:
   * coffe
   * tea
   * cup
   * sugar

## BookJourney
a) For a correct usage: run the bookJourney_ok.py script and follow the instructions in each client windwow

b) To see how a handled wrongError branch is carried out: run bookJourney_wrong.py . There will be a payload error the first time around, but the second iteration sends the right one.


