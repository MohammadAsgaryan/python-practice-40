# ------------------------------------------
#   Simple To-Do Manager
#   Author: You
#   Description:
#       A command-line task manager that lets
#       users create, view, delete, and search
#       tasks. All data is stored inside a text
#       file (tasks.txt).
# ------------------------------------------

TASK_FILE = "tasks.txt"


def add_task():
    """Add a new task to the file."""
    task = input("Enter new task: ").strip()

    if not task:
        print("Task cannot be empty!")
        return

    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")

    print("Task added successfully.")


def show_tasks():
    """Display all tasks."""
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print("No tasks found.")
        return

    if not tasks:
        print("Your task list is empty.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")
    print("-------------------\n")


def delete_task():
    """Delete a task by its number."""
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print("No tasks found.")
        return

    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks()
    choice = input("Enter the task number to delete: ")

    if not choice.isdigit():
        print("Invalid number.")
        return

    index = int(choice)

    if not (1 <= index <= len(tasks)):
        print("Number out of range.")
        return

    removed_task = tasks.pop(index - 1)

    with open(TASK_FILE, "w", encoding="utf-8") as file:
        file.writelines(tasks)

    print(f"Deleted: {removed_task.strip()}")


def search_task():
    """Search for tasks containing a keyword."""
    keyword = input("Enter a keyword to search: ").strip().lower()

    if not keyword:
        print("Keyword cannot be empty!")
        return

    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print("No tasks found.")
        return

    found = [t.strip() for t in tasks if keyword in t.lower()]

    if not found:
        print("No matching tasks found.")
        return

    print("\n--- Search Results ---")
    for t in found:
        print("- " + t)
    print("----------------------\n")


def main():
    while True:
        print("""
===== TO-DO MANAGER =====
1. Add Task
2. Show Tasks
3. Delete Task
4. Search Task
5. Exit
=========================
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
