import json

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

tasks = []
last_task_id = 0  

def add_task(title):
    global last_task_id
    last_task_id += 1 
    task = Task(last_task_id, title)
    tasks.append(task)

def view_tasks():
    for task in tasks:
        status = 'Completed' if task.completed else 'Pending'
        print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

def delete_task(task_id):
    global tasks
    
    new_tasks = []
    for task in tasks:
        if task.id != task_id:
            new_tasks.append(task)
    tasks = new_tasks  

def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True

def save_tasks():
    task_dicts = []
    for task in tasks:
        task_dicts.append(task.__dict__)  
    with open('tasks.json', 'w') as f:
        json.dump(task_dicts, f)

def load_tasks():
    global tasks, last_task_id
    try:
        with open('tasks.json', 'r') as f:
            tasks_data = json.load(f)
            tasks = []  
            for data in tasks_data:
                task = Task(data['id'], data['title'], data['completed'])
                tasks.append(task)
            if tasks:
               
                last_task_id = max(task.id for task in tasks)
    except FileNotFoundError:
        tasks = []

def cli_menu():
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to complete: "))
            complete_task(task_id)
        elif choice == '5':
            save_tasks()
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

DUMMY_EMAIL = "test@mnk.com"
DUMMY_PASSWORD = "test123"

def login():
    print("Please log in to access the Task Manager")
    email = input("Email: ")
    password = input("Password: ")

    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Exiting program.")
        return False

if login():
    load_tasks()
    cli_menu()
