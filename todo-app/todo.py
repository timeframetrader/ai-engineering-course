tasks = []

while True:
    choice = input("\nWhat do you want to do? (add / view / remove / quit): ").strip().lower()

    if choice == "add":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "view":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])

    elif choice == "remove":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            number = input("Enter task number to remove: ")
            if number.isdigit() and 1 <= int(number) <= len(tasks):
                removed = tasks.pop(int(number) - 1)
                print("Removed: " + removed)
            else:
                print("Invalid number.")

    elif choice == "quit":
        print("Goodbye!")
        break

    else:
        print("I don't understand that. Try: add, view, remove, or quit.")
