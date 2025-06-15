from ortools.sat.python import cp_model

def generate_schedule(staff, shift_requirements, constraints):
    model = cp_model.CpModel()
    shifts = {}
    all_staff = [s.name for s in staff]
    all_days = list(set([sr.date for sr in shift_requirements]))

    for day in all_days:
        for shift_type in ["Morning", "Evening"]:
            for person in all_staff:
                shifts[(day, shift_type, person)] = model.NewBoolVar(f"{day}_{shift_type}_{person}")

    for sr in shift_requirements:
        date, shift_name, needed = sr.date, sr.shift, sr.needed
        model.Add(sum(shifts[(date, shift_name, person)] for person in all_staff) == needed)

    for name, settings in constraints.items():
        for u in settings.get('unavailable', []):
            model.Add(shifts[(u['date'], "Morning", name)] == 0)
            model.Add(shifts[(u['date'], "Evening", name)] == 0)

        if settings.get('max_shifts'):
            model.Add(
                sum(shifts[(day, shift, name)] for day in all_days for shift in ["Morning", "Evening"]) <= settings['max_shifts']
            )

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    result = []
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        for day in sorted(all_days):
            shifts_today = {}
            for shift_type in ["Morning", "Evening"]:
                people = [
                    person for person in all_staff
                    if solver.Value(shifts[(day, shift_type, person)]) == 1
                ]
                shifts_today[shift_type] = people
            result.append({"date": day, "shifts": shifts_today})

    return result