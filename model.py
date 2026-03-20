from pydantic import BaseModel
from datetime import datetime

class Equipment(BaseModel):
    id: int
    name: str
    type: str
    status: str
    room: str

class Movement(BaseModel):
    id: int
    equipment_id: int
    from_room: str
    to_room: str
    date: datetime




