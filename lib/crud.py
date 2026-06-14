# CRUD realization JSON file
from lib.json import work_with_json_file
import uuid

class Task:
    list = work_with_json_file("data/tasks.json", mode="r")

    def validate_task_number(task_number):
        if task_number < 0 or task_number >= len(Task.list):
            print("\033[31mInvalid task ID.\033[0m")
            return False
        return True

    def create_task(task_name):
        
        uuid4 = uuid.uuid4()

        new_task = {
            "id": str(uuid4),
            "title": task_name,
            "completed": False
        }

        Task.list.append(new_task)

        work_with_json_file("data/tasks.json", data=Task.list, mode="w")

    def view_tasks():

        if not Task.list:
            print("\033[31mNo tasks found.\033[0m \033[32mCreate a new task to get started!\033[0m")
            return

        for i, task in enumerate(Task.list):
            status = f"\033[32m✓\033[0m" if task["completed"] else f"\033[31m✗\033[0m"
            print(f"id:({i}) {task['title']} {status}")

    def update_task(task_number, new_task_name):

        if not Task.validate_task_number(task_number): return


        Task.list[task_number]["title"] = new_task_name

        work_with_json_file("data/tasks.json", data=Task.list, mode="w")

    def complete_task(task_number):

        if not Task.validate_task_number(task_number): return

        Task.list[task_number]["completed"] = not Task.list[task_number]["completed"]
        print(f"{Task.list[task_number]['title']} is {'completed' if Task.list[task_number]['completed'] else 'not completed'}")

        work_with_json_file("data/tasks.json", data=Task.list, mode="w")

    def delete_task(task_number):

        if not Task.validate_task_number(task_number): return

        del Task.list[task_number]

        work_with_json_file("data/tasks.json", data=Task.list, mode="w")
        print(f"Task ID '{task_number}' deleted successfully!")