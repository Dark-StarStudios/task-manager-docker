# Application
import getpass
from lib.crud import create_task, view_tasks, update_task, delete_task

exit = False
username = getpass.getuser()
print(f"Hello: {username}.")
print("Welcome to the Task Manager Application!")


while exit == False:
    print("1. Create a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

    input_choice = input("Please enter your choice (1-5): ")
    if input_choice == "1":
        task_name = input("Enter the task name: ")
        create_task(task_name)
        print(f"Task '{task_name}' created successfully!")
    elif  input_choice == "2":
        print("-----------------------------------------------------------------------")
        view_tasks()
    elif input_choice == "3":
        view_tasks()
        task_number = input("Enter the task ID to update: ")
        new_task_name = input("Enter the new task name: ")
        update_task(int(task_number), new_task_name)
        print(f"Task'{task_number}' updated successfully to '{new_task_name}'!")
    elif input_choice == "4":
        task_number = input("Enter the task ID to delete: ")
        delete_task(int(task_number))
        print(f"Task ID '{task_number}' deleted successfully!")
    else:
        print("Exiting the application. Goodbye!")
        exit = exit = True
    print("-----------------------------------------------------------------------")

