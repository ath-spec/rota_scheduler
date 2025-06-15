from fastapi import APIRouter, HTTPException
from schemas.models import ScheduleRequest
from services.scheduler_service import generate_schedule
from services.llama_parser import parse_constraints

router = APIRouter()

@router.post("/generate-schedule/")
async def create_schedule(request: ScheduleRequest):
    try:
        parsed_constraints = parse_constraints(request.constraints)
        schedule = generate_schedule(request.staff, request.shift_requirements, parsed_constraints)
        return schedule
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))