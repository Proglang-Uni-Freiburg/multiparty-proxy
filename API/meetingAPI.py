from fastapi import FastAPI, Response, status, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Any


# -- API ------------------------------------------------------
app = FastAPI()

class Meeting(BaseModel):
    actors: list[str]
    protocol: str

class MeetingInfo(BaseModel):
    meeting_id: str
    port: int

meetingDict: dict[str, Meeting] = {}
meeting_info_store: dict[str, MeetingInfo] = {}
lastID = "0"
proxy_port = 0 # temporary

# create a meeting -> register and give back meeting ID
@app.post("/meetings/", response_model=MeetingInfo)
async def createMeetingReq(meeting: Meeting) -> MeetingInfo: # why Any?
    global lastID
    lastID = str(int(lastID) + 1)
    meetingDict[lastID] = meeting
    info = MeetingInfo(meeting_id=lastID, port=proxy_port)
    meeting_info_store[lastID] = info
    return info

@app.get("/meetings/{meeting_id}/", response_model=MeetingInfo)
async def getMeetingReq(meeting_id:str) -> MeetingInfo:
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    return meeting_info_store[meeting_id]

@app.get("/meetings/{meeting_id}/{actors}", response_model=str)
async def getMeetingReq(meeting_id:str) -> str:
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    return "" # temporary; return local protocol projection

@app.delete("/meetings/{meeting_id}")
async def deleteMeetingReq(meeting_id: str) -> Response:
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    del meetingDict[meeting_id]
    del meeting_info_store[meeting_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # should return ok but idk how it works

# -- to store/create info --------------------------------------

# make a func. to create better meeting IDs
# def createMeetingID() -> str:

# checks protocols

# 1. create .src file with protocol
# 2. uses scribble tool to parse it
# 3. outputs .json (could also be .fsm and .java, but ig json make more sense to send to proxy!)
