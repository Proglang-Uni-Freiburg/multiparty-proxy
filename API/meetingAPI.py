# API imports
from fastapi import FastAPI, Response, status, HTTPException, Request, Body
# import uvicorn
from pydantic import BaseModel

# for type annotations
from typing import Any, List, Mapping

# imports to be able to use functions from other modules in project or access files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import os

# functions in project
from tools.get_port import get_free_port # for finding a free port for the proxy
from tools.json_to_scribble import json_to_scribble_func
from scribble_python.wf_checker import check_well_formedness, WellFormednessError # check Scribble protocol
from proxy.session_logic.type_validation import create_type_checker # for payload type schemas

# proxy imports
import threading # for handling several proxies
from proxy.proxy import main_proxy

# -- initialize ----------------------------------------------------------------------
app = FastAPI()

# models for receiving info through API requests
class Role(BaseModel):
    name: str
    alias: str

class Meeting(BaseModel):
    protocol: str # name of protocol
    roles: List[Role] # actors in protocol
    body: List[Any]  # protocol definition
    error: str = "fatal" # type of error (fatal, ignore, handle)
    timeout: float = 60.0

# dicts for storing meetings info
meetingDict: dict[str, Meeting] = {} # name of meeting : meeting object
meeting_info: dict[str, int] = {} # name of meeting : assigned proxy port
current_json:Any = {}  # to store the current json protocol
meeting_types:dict[str, list[Any]] = {} # meeting name: schema list
# for handling several proxies
proxy_threads = {}  # meeting name : thread

# -- API ---------------------------------------------------------------------------------------------------

# create a meeting -> register and give back corresponding proxy port
@app.post("/meetings/", response_model=int)
async def createMeetingReq(meeting: Meeting, request: Request):
    # check no repeated meeting names
    if meeting.protocol in meetingDict:
        raise HTTPException(status_code=409, detail="Meeting already exists")
    
    # check if error type was defined and if defined ok, set; if not defined, use default
    if meeting.error:
        if meeting.error not in ("fatal", "ignore", "handle"):
            raise HTTPException(status_code=422, detail="Error must be 'ignore', 'fatal' or 'handle'")

    # zero: define types
    print(f"defning meeting protocol: {meeting.protocol}") # debug
    schemas: list[Any]
    if meeting.protocol in meeting_types:
        # print(f"found schemas in {meeting.protocol}") # debug
        schemas = meeting_types[meeting.protocol]
    else:
        schemas = []
    types: tuple[dict[str, Any], dict[str, Any]]
    types = create_type_checker(schemas) # all type schemas we'll need for types in protocol

    # one: transform to scr
    current_json = await request.json()
    json_to_scribble_func(path="API/protocols", proto=current_json, schemas=types) # TODO: add try block
    # join dicts of schemas of builtin and custom types into one dict
    merged_types = types[0].copy()
    merged_types.update(types[1])

    # two: check if protocol is well-formed
    try:
        check_well_formedness(f"API/protocols/{meeting.protocol}.scr")
    except WellFormednessError as e:
        os.remove(f"API/protocols/{meeting.protocol}.scr")
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=f"Invalid protocol: {e}")
    
    # three: find free port for proxy
    proxy_port = get_free_port()

    # four: store meeting info
    meetingDict[meeting.protocol] = meeting
    proxy_port = get_free_port()
    meeting_info[meeting.protocol] = proxy_port
    
    # five: create proxy for meeting
    actors = [(role.name, role.alias) for role in meeting.roles]
    def run_proxy():
        import asyncio
        asyncio.run(main_proxy(proxy_port, actors, meeting.protocol, merged_types, meeting.error, meeting.timeout))
    thread = threading.Thread(target=run_proxy, daemon=True)
    thread.start()
    proxy_threads[meeting.protocol] = thread

    # six: give back port number
    return proxy_port

# so that others can find out port based on meeting name
@app.get("/meetings/{meeting_name}/", response_model=int)
async def getMeetingReq(meeting_name:str) -> int:
    if meeting_name not in meetingDict:
        raise HTTPException(404, "Not found")
    return meeting_info[meeting_name]

# allows definition of JSON schemas for types used in a meeting
# TODO:for now schemas one by one but later as a batch
@app.post("/types/{meeting_name}/")
async def createType(meeting_name: str, schema:Mapping[str, Any]= Body(...)): # TODO: why Any?
    print(f"defining: {schema.get('title')} for {meeting_name}") # debug
    if meeting_name not in meeting_types: # for first custom schema in a meeting
        meeting_types[meeting_name] = []
    meeting_types[meeting_name].append(schema)

# for deleting a meeting once it is done
@app.delete("/meetings/{meeting_name}")
async def deleteMeetingReq(meeting_name: str):
    if meeting_name not in meetingDict:
        raise HTTPException(404, "Not found")
    print(f"Deleting meeting {meeting_name}...") # debug
    del meetingDict[meeting_name]
    del meeting_info[meeting_name]
    meeting_types.pop(meeting_name, None) # pop because it might be empty and pop doesn't throw error if so
    os.remove(f"API/protocols/{meeting_name}.scr")
    return Response(status_code=status.HTTP_204_NO_CONTENT) # TODO: check this is the right thing to return

# TODO: determine if this is necessary
"""
@app.get("/meetings/{meeting_id}/{actors}", response_model=str)
async def getMeetingReq(meeting_id:str) -> str:
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    return "" # temporary; return local protocol projection
"""

