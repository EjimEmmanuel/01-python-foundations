import json

FILE_PATH = "data/statistics.json"

def dump_statistics(statistics):
    try:
        with open(FILE_PATH, "w") as f:
            return json.dump(statistics, f, indent=4)
    except FileExistsError:
        return {}
    except json.JSONDecodeError:
        return {}

    
def initialize_statistics():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
