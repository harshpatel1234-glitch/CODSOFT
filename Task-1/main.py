def display_options():
    print("\n--- My To-Do App ---")
    print("A. Add a new task")
    print("B. View tasks")
    print("C. Delete a task")
    print("D. Exit")


def add_new_task(todo_items):
    tasks = input("Enter task name: ").strip()
    if tasks:
        todo_items.append(tasks)
        print(" Task saved.")
    else:
        print(" Empty task not allowed.")


def show_tasks(todo_items):
    if len(todo_items) == 0:
        print("Task list is empty.")
    else:
        print("\nPending Tasks:")
        count = 1
        for item in todo_items:
            print(f"{count}. {item}")
            count += 1


def remove_task(todo_items):
    if not todo_items:
        print("No task to remove.")
        return

    show_tasks(todo_items)

    try:
        pos = int(input("Enter task number to delete: "))
        if 1 <= pos <= len(todo_items):
            deleted = todo_items.pop(pos - 1)
            print(f"Task '{deleted}' removed.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a number only.")


def run_app():
    todo_list = []

    while True:
        display_options()
        user_choice = input("Choose option (A-D): ").upper()

        if user_choice == "A":
            add_new_task(todo_list)

        elif user_choice == "B":
            show_tasks(todo_list)

        elif user_choice == "C":
            remove_task(todo_list)

        elif user_choice == "D":
            print("App closed successfully.")
            break

        else:
            print("Wrong option selected.")

run_app()
