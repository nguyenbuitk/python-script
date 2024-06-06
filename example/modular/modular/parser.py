def parse(feet_inches):
    parts = feet_inches.split()
    feet = int(parts[0])
    inches = int(parts[1])
    return {"feet": feet, "inches": inches}
