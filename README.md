# Task Manager

A small console Task Manager application written in Python.

## Requirements
- Python 3.10.10
- Docker

## Run locally
```bash
python app.py
```

## Run with Docker
```bash
docker build -t task-manager .
docker run -it task-manager
```

## Design choices
- Task represents a single task with UUID, title, and completion status.
- Class Task handles task operations and JSON persistence.
- JSON is used because it is simple and available in the Python standard library.
- The console menu is separated from task crud logic for readability.