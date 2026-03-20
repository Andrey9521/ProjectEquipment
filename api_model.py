from fastapi import FastAPI
from typing import List
from datetime import datetime
from model import Equipment, Movement

app = FastAPI()
equipment_list: List[Equipment] = []
movements: List[Movement] = []


@app.get("/equipment")
def get_equipment():
    return equipment_list

@app.post("/add_equipment")
def add_equipment(equipment: Equipment):
    equipment_list.append(equipment)
    return {"message": "Обладнання додано", "equipment": equipment}

@app.put("/equipment/{equipment_id}/status")
def add_equipment_status(equipment_id: int, status: str):
    for equipment in equipment_list:
        if equipment.id == equipment_id:
            equipment.status = status
            return {"message": "Статус оновлено", "equipment": equipment}
    return {"error": "Обладнання не знайдено"}

@app.put("/equipment/{equipment_id}/move")
def move_equipment(equipment_id: int, new_room: str):

