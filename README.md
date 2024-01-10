# ToDoList Application

Manage tasks and subtasks in a JSON file.

Author: Bratchik Oleg
Date: 29-12-2023

## Overview

The ToDoList application is a simple task management console program written in Python. It allows users to add, remove, mark tasks as done, add subtasks, set deadlines, and view the list of tasks. Tasks and their details are stored in a JSON file, providing persistence across program executions.

## Features

- **Add Tasks:** Add new tasks with optional deadlines.
- **Remove Tasks:** Delete tasks from the list.
- **Mark Tasks as Done:** Toggle the status of tasks between done and not done.
- **Add Subtasks:** Attach subtasks to existing tasks.
- **Set Deadlines:** Change the deadline of a task.
- **View Tasks:** Display the list of tasks along with their details.

## Usage

1. Run the program by executing the `concole.py` file.
2. Follow the on-screen menu to perform various actions.
3. Input numbers corresponding to the desired action.

## Examples

```bash
# Add a new task
1. Add Task
Enter task title: Your Task Title
Enter task deadline (YYYY-MM-DD): 2024-01-31

# Mark a task as done
3. Mark Task as Done
Enter task number to mark as done: 1

# Add a subtask to an existing task
4. Add Subtask
Enter task number to add subtask: 1
Enter subtask title: Your Subtask Title
