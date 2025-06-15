from pydantic import BaseModel
from typing import List

class Staff(BaseModel):
    name: str

class ShiftRequirement(BaseModel):
    date: str
    shift: str
    needed: int

class ScheduleRequest(BaseModel):
    staff: List[Staff]
    shift_requirements: List[ShiftRequirement]
    constraints: List[str]