# Task Manager CLI Application

## Project Description
This project is a command-line interface (CLI) application for managing tasks. Users can add, view, delete, and mark tasks as complete. The application saves tasks to a JSON file, allowing persistence across sessions. A simple login with dummy credentials has been added to control access to the Task Manager.

## Features
- **Add Task**: Allows users to add a new task to the task list with a unique ID.
- **View Tasks**: Displays all tasks, along with their ID, title, and completion status.
- **Delete Task**: Enables users to delete a task by specifying its ID.
- **Mark Task as Complete**: Allows users to mark a task as completed by entering its ID.
- **Save Tasks**: Saves all tasks to `tasks.json` to persist the task list across sessions.
- **Load Tasks**: Loads tasks from `tasks.json` when the application starts.
- **Login System**: Basic login with dummy credentials to access the Task Manager.

## Dummy Login Credentials
To access the application, use the following login credentials:
- **Email**: `test@mnk.com`
- **Password**: `test123`

## How to Run the Application
1. **Clone the repository**:
   ```bash
   git clone <https://github.com/murshidalam7474/Task-Manager-CLI-Application/>
   cd task_manager
