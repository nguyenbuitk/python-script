import os

TODO_FILE = 'todo_list.txt'

def load_tasks():
    """Load tasks from the file and return them as list."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks to show.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def remove_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove"))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Task '{remove_task}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-do List Menu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

