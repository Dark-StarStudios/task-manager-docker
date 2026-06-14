# CRUD realization JSON file
from lib.json import work_with_json_file
import uuid


def create_task(task_name):
    tasks = work_with_json_file("data/tasks.json", mode="r")
    uuid4 = uuid.uuid4()

    new_task = {
        "id": str(uuid4),
        "title": task_name,
        "completed": False
    }

    tasks.append(new_task)

    work_with_json_file("data/tasks.json", data=tasks, mode="w")

def view_tasks():
    tasks = work_with_json_file("data/tasks.json", mode="r")

    if not tasks:
        print("No tasks found. Create a new task to get started!")
        return

    for i, task in enumerate(tasks):
        print(f"id:({i}) {task['title']} {'✓' if task['completed'] else '✗'}")

def update_task(task_number, new_task_name):
    tasks = work_with_json_file("data/tasks.json", mode="r")

    if task_number < 0 or task_number >= len(tasks):
        print("Invalid task ID.")
        return


    tasks[task_number]["title"] = new_task_name

    work_with_json_file("data/tasks.json", data=tasks, mode="w")

def complete_task(task_number):
    tasks = work_with_json_file("data/tasks.json", mode="r")

    if task_number < 0 or task_number >= len(tasks):
        print("Invalid task ID.")
        return

    tasks[task_number]["completed"] = not tasks[task_number]["completed"]
    print(f"{tasks[task_number]['title']} is {'completed' if tasks[task_number]['completed'] else 'not completed'}")

    work_with_json_file("data/tasks.json", data=tasks, mode="w")

def delete_task(task_id):
    tasks = work_with_json_file("data/tasks.json", mode="r")

    if task_id < 0 or task_id >= len(tasks):
        print("Invalid task ID.")
        return

    del tasks[task_id]

    work_with_json_file("data/tasks.json", data=tasks, mode="w")