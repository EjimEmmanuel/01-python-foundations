import json

FILE_PATH = "data/statistics.json"

def dump_statistics(statistics, file_path=FILE_PATH):                    
    try:
        with open(file_path, "w") as f:
            return json.dump(statistics, f, indent=4)
    except FileExistsError:
        return {}
    except json.JSONDecodeError:
        return {}

    
def initialize_statistics(file_path=FILE_PATH):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
