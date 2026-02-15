tasks = []


# load tasks from file (if file exists)
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except FileNotFoundError:
    pass   # file does not exist yet


while True:
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # VIEW TASKS
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # ADD TASK
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)

        file = open("tasks.txt", "w")
        for t in tasks:
            file.write(t + "\n")
        file.close()

        print("Task added.")

    # REMOVE TASK
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)

                file = open("tasks.txt", "w")
                for t in tasks:
                    file.write(t + "\n")
                file.close()

                print("Removed:", removed)

            except:
                print("Invalid input.")

    # EXIT
    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
