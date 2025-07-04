from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import schedule

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(schedule.router)