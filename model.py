from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Equipment(BaseModel):
    id: Optional[int] = None
    name: str
    type: str
    status: str
    room: str

    def to_dict(self) -> dict:
        return self.dict()


class Movement(BaseModel):
    id: int
    equipment_id: int
    from_room: str
    to_room: str
    date: datetime

    def to_dict(self) -> dict:
        return self.dict()


class Problem(BaseModel):
    id: int
    equipment_id: int
    description: str
    date: datetime

    def to_dict(self) -> dict:
        return self.dict()



