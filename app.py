# Application
import getpass
from lib.crud import Task

exit = False
username = getpass.getuser()
print(f"Hello: {username}.")
print("Welcome to the Task Manager Application!")


while exit == False:
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Edit task")
    print("or any other key to exit")

    input_choice = input("Please enter your choice (1-5): ")
    if input_choice == "1":
        task_name = input("Enter the task name: ")
        Task.create_task(task_name)
        print(f"Task '{task_name}' created successfully!")
    elif  input_choice == "2":
        print("-----------------------------------------------------------------------")
        Task.view_tasks()
    elif input_choice == "3":
        Task.view_tasks()
        task_number = input("Enter the task ID to complete: ")
        Task.complete_task(int(task_number))
    elif input_choice == "4":
        Task.view_tasks()
        task_number = input("Enter the task ID to delete: ")
        Task.delete_task(int(task_number))
    elif input_choice == "5":
        Task.view_tasks()
        task_number = input("Enter the task ID to edit: ")
        new_task_name = input("Enter the new task name: ")
        Task.update_task(int(task_number), new_task_name)
    else:
        print("Exiting the application. Goodbye!")
        exit = exit = True
    print("-----------------------------------------------------------------------")

