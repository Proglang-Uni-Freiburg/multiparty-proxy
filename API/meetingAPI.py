from fastapi import FastAPI, Response, status, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Any


# -- API ------------------------------------------------------
app = FastAPI()

class Meeting(BaseModel):
    actors: list[str]
    protocols: list[str]

meetingDict: dict[str, Meeting] = {}
lastID = "0"

# create a meeting -> register and give back meeting ID
@app.post("/meetings/", response_model=str)
async def createMeetingReq(meeting: Meeting) -> str: # why Any?
    global lastID
    lastID = str(int(lastID) + 1)
    meetingDict[lastID] = meeting
    return lastID

@app.get("/meetings/{meeting_id}", response_model=Meeting)
async def getMeetingReq(meeting_id:str) -> Meeting: # why Any?
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    return meetingDict[meeting_id]

@app.delete("/meetings/{meeting_id}")
async def deleteMeetingReq(meeting_id: str) -> Response: # why Any?
    if meeting_id not in meetingDict:
        raise HTTPException(404, "Not found")
    del meetingDict[meeting_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # should return ok but idk how it works

# -- to store/create info --------------------------------------

# make a func. to create better meeting IDs
# def createMeetingID() -> str:
