# Directory structure overview:
# restaurant-scheduler/
# ├── backend/
# ...
# scheduler/service.py
from ortools.sat.python import cp_model
from datetime import datetime

...

    return result