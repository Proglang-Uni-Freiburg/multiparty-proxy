from fastapi import FastAPI, Response, status, HTTPException, Request, Body
import uvicorn
from pydantic import BaseModel
from typing import Any, List, Mapping

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import os

from tools.get_port import get_free_port
from tools.json_to_scribble import transform
from scribble_python.wf_checker import check_well_formedness, WellFormednessError

# fro handling several proxies
import threading
from proxy.proxy import main_proxy

from proxy.session_logic.type_validation import create_type_checker

# -- API ------------------------------------------------------
app = FastAPI()

class Role(BaseModel):
    name: str
    alias: str

class Meeting(BaseModel):
    protocol: str
    roles: List[Role]
    body: List[Any]  # steps, for now


# dicts for storing meetings info
meetingDict: dict[str, Meeting] = {}
meeting_info: dict[str, int] = {}
current_json:dict = None  # to store the current json protocol
meeting_types:dict[str, list] = {} # meeting name: schema list 

# for handling several proxies
proxy_threads = {}  # meeting name -> thread


# create a meeting -> register and give back meeting ID
@app.post("/meetings/", response_model=int)
async def createMeetingReq(meeting: Meeting, request: Request) -> int: # why Any?
    # zero: define types
    print(f"meeting protocol: {meeting.protocol}") # debug
    if meeting.protocol in meeting_types:
        print(f"found schemas in {meeting.protocol}") # debug
        schemas = meeting_types[meeting.protocol]
        print(f"schemas: {schemas}") # debug
    else:
        schemas = None
    types = create_type_checker(schemas)
    print(types) # debug

    # one: transform to scr
    current_json = await request.json()
    transform(current_json, types, output_dir="API/protocols")
    # two: check if protocol is well-formed
    try:
        check_well_formedness(f"API/protocols/{meeting.protocol}.scr")
    except WellFormednessError as e:
        os.remove(f"API/protocols/{meeting.protocol}.scr")
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=f"Invalid protocol: {e}")
    # three: find free port
    proxy_port = get_free_port()
    # four: store meeting info and schemas
    meetingDict[meeting.protocol] = meeting
    proxy_port = get_free_port()
    meeting_info[meeting.protocol] = proxy_port

    
    # five: create proxy for meeting
    actors = [(role.name, role.alias) for role in meeting.roles]
    def run_proxy():
        import asyncio
        asyncio.run(main_proxy(proxy_port, actors, meeting.protocol, types))
    thread = threading.Thread(target=run_proxy, daemon=True)
    thread.start()
    proxy_threads[meeting.protocol] = thread
    # six: give back port number
    return proxy_port

# so that others can find out port based on meeting name
@app.get("/meetings/{meeting_id}/", response_model=int)
async def getMeetingReq(name:str) -> int:
    if name not in meetingDict:
        raise HTTPException(404, "Not found")
    return meeting_info[name]

# for now schemas one by one but later as a batch
@app.post("/types/{meeting_name}/")
async def createMeetingReq(meeting_name: str, schema:Mapping[str, Any]= Body(...)): # why Any?
    print(f"defining: {schema} for {meeting_name}") # debug
    if meeting_name not in meeting_types:
        meeting_types[meeting_name] = []
    meeting_types[meeting_name].append(schema)


"""
@app.get("/meetings/{meeting_id}/{actors}", response_model=str)
async def getMeetingReq(meeting_id:str) -> str:
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    return "" # temporary; return local protocol projection
"""

@app.delete("/meetings/{meeting_id}")
async def deleteMeetingReq(meeting_id: str) -> Response:
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    del meetingDict[meeting_id]
    del meeting_info[meeting_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # should return ok but idk how it works
