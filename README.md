# Assignment: Build a Small "Task Manager" Console Application in Python running in a Docker container

## Description

Create a console application in Python 3, that allows a
user to manage a list of tasks.

The user should be able to:

1. Add a new task
2. List all tasks
3. Mark a task as completed
4. Delete a task
5. Save tasks to a file (persistent storage)
6. Load tasks when the program starts

# Functional Requirements

## Task Model

Each task must include:

- A unique ID (UUID)
- A title (string)
- A "completed" status (boolean)

# Technical Requirements

## Docker

- Use Docker to create a container image with Python and the code of the application
- A Docker container from the image should directly run the application when started 

## Python

- Use Python 3.9 or later.
- Use only the standard library (no external packages required).
- Structure your code using functions or classes.
- Use US English for the interface and internal variable and function names

## Data Storage

- Use a JSON file to store tasks
- When the program starts:
  - Load tasks from the file if it exists.
  - Otherwise, start with an empty list.
- After any change, save tasks back to the file.

## Command-Line Menu

Implement a menu such as:

```
    1. Add task
    2. List tasks
    3. Complete task
    4. Delete task
    5. Exit
```

The user selects an action by entering a number.

## Git Requirements

- Place all source code in a Git repository.
- Use meaningful commit messages.
- Submit the project as a Git archive created using the `archive` sub-command

# Deliverables

A Git repository containing:
1. Python source code (`.py` files).
2. A `README.md` file with:
   - Instructions for running the program
   - Python version used
   - A short description of design choices

# Optional (Bonus) Features

These are not required, but can give a stronger impression:

- Edit an existing task
- Sort tasks (by status, title, etc.)
- Colorful console output using ANSI escape codes
- Input validation
- A class-based structure (`Task`, `TaskManager`)