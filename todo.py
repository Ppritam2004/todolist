def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit\n")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added!")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("\nEnter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"❌ Task '{removed}' removed!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid option. Please try again.")

if __name__ == "__main__":
    main()