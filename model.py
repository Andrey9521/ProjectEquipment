from pydantic import BaseModel
from datetime import datetime

class Equipment(BaseModel):
    id: int
    name: str
    type: str
    status: str
    room: str

    def to_json(self) -> str:
        return self.json()


class Movement(BaseModel):
    id: int
    equipment_id: int
    from_room: str
    to_room: str
    date: datetime

    def to_json(self) -> str:
        return self.json()


class Problem(BaseModel):
    id: int
    equipment_id: int
    description: str
    date: datetime

    def to_json(self) -> str:
        return self.json()



