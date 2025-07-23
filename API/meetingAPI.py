from fastapi import FastAPI, Response, status, HTTPException, Request
import uvicorn
from pydantic import BaseModel
from typing import Any, List

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools.get_port import get_free_port
from tools.json_to_scribble import transform
from scribble_python.wf_checker import check_well_formedness


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


# create a meeting -> register and give back meeting ID
@app.post("/meetings/", response_model=int)
async def createMeetingReq(meeting: Meeting, request: Request) -> int: # why Any?
    # one: transform to scr
    current_json = await request.json()
    transform(current_json, output_dir="protocols")
    # two: check if protocol is well-formed
    try:
        check_well_formedness(f"protocols/{meeting.protocol}.scr")
    except Exception as e:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=f"Invalid protocol: {e}")
    # three: find free port
    proxy_port = get_free_port()
    # four: store meeting info
    meetingDict[meeting.protocol] = meeting
    proxy_port = get_free_port()
    meeting_info[meeting.protocol] = proxy_port
    # five: create proxy for meeting
    # create_proxy()
    # five: give back port number
    return proxy_port

# so that others can find out port based on meeting name
@app.get("/meetings/{meeting_id}/", response_model=int)
async def getMeetingReq(name:str) -> int:
    if name not in meetingDict:
        raise HTTPException(404, "Not found")
    return meeting_info[name]

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

# -- to store/create info --------------------------------------

# make a func. to create better meeting IDs
# def createMeetingID() -> str:

# checks protocols

# 1. create .src file with protocol
# 2. uses scribble tool to parse it
# 3. outputs .json (could also be .fsm and .java, but ig json make more sense to send to proxy!)
