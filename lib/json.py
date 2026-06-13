import json
from pathlib import Path


def ensure_json_file(file_path):
    path = Path(file_path)

    # Create folder if it does not exist
    path.parent.mkdir(parents=True, exist_ok=True)

    # Create JSON file if it does not exist
    if not path.exists():
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

def work_with_json_file(file_path, data=None, mode='r'):
    ensure_json_file(file_path)
        
    if mode == 'r':
        with open(file_path, 'r') as file:
            return json.load(file)
    elif mode == 'w':
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)