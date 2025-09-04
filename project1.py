# Simple To-Do List Manager 

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")   # i+1 for numbering tasks

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")