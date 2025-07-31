from pydantic import BaseModel
from typing import Optional
from enum import Enum

#creating a thing called as Status Enum which basically is ti limit it by saying that only 2 options can be given as open or close and used below
class StatusEnum(str, Enum):
    open = "open"
    closed = "closed"

#here we mainly work n see that inputs are taken an stauts will hv only 2 ways open/closed but if nothing is seen ,take it as open(complaint not yet closed)
class Complaint(BaseModel):
    id: int
    title: str
    description: str
    #this mainly means that we can have the location in the field and even without it the output will be shown if the location is not specified
    location: Optional[str] = None
    status: StatusEnum = StatusEnum.open
