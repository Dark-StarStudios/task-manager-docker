# Application
import getpass

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
        # Here you would add code to save the task to JSON file
        print(f"Task '{task_name}' created successfully!")
    elif  input_choice == "2":
        # Here you would add code to read and display tasks from JSON file
        print("Displaying all tasks...")
    elif input_choice == "3":
        task_id = input("Enter the task ID to update: ")
        new_task_name = input("Enter the new task name: ")
        # Here you would add code to update the task in JSON file
        print(f"Task ID '{task_id}' updated successfully to '{new_task_name}'!")
    elif input_choice == "4":
        task_id = input("Enter the task ID to delete: ")
        # Here you would add code to delete the task from JSON file
        print(f"Task ID '{task_id}' deleted successfully!")
    else:
        print("Exiting the application. Goodbye!")
        exit = exit = True

