from fastapi import FastAPI
from typing import List
from datetime import datetime
from model import Equipment, Movement, Problem

app = FastAPI()
equipment_list: List[Equipment] = []
movements: List[Movement] = []
problems: List[Problem] = []


@app.get("/equipment")
def get_equipment():
    return [equipment.to_json() for equipment in equipment_list]

@app.post("/add_equipment")
def add_equipment(equipment: Equipment):
    equipment_list.append(equipment)
    return {"message": "Обладнання додано", "equipment": equipment.to_json()}

@app.put("/equipment/{equipment_id}/status")
def add_equipment_status(equipment_id: int, status: str):
    for equipment in equipment_list:
        if equipment.id == equipment_id:
            equipment.status = status
            return {"message": "Статус оновлено", "equipment": equipment}
    return {"error": "Обладнання не знайдено"}

@app.put("/equipment/{equipment_id}/move")
def move_equipment(equipment_id: int, new_room: str):
    for equipment in equipment_list:
        if equipment.id == equipment_id:
            movement = Movement(
                id = len(movements) + 1,
                equipment_id = equipment_id,
                from_room = equipment.room,
                to_room = new_room,
                date = datetime.now(),
            )
            movements.append(movement)
            equipment.room = new_room
            return {"message": "Обладнання переміщено", "movement": movement.to_json()}
    return {"error": "Обладнання не знайдено"}

@app.get("/equipment/{equipment_id}/problems")
def get_problems(equipment_id: int):
    return [p.to_json() for p in problems if p.equipment_id == equipment_id]

@app.post("/equipment/{equipment_id}/problem")
def add_problem(equipment_id: int, description: str):
    problem = Problem(
        id=len(problems)+1,
        equipment_id=equipment_id,
        description=description,
        date=datetime.now()
    )
    problems.append(problem)
    return {"message": "Проблему додано", "problem": problem.to_json()}

@app.get("/equipment/search")
def search_equipment(name: str):
    return [eq.to_json() for eq in equipment_list if name.lower() in eq.name.lower()]




