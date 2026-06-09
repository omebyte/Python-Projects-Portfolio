tasks = []
# Load tasks from file (if it exists)
try:
    with open("tasks.txt", "r") as file:    # This opens a file called tasks.txt    "w(write mode)" ovewrites the file each time    "as file" givesa us a variable 'file' to work with inside this block
         tasks = [line.strip() for line in file]        #with" automatically closes the file when done (so we don't forget)
except FileNotFoundError:
     tasks = [] #Start with empty list if no task yet
while True:
    print("\n1. Add Task")
    print("2. View all tasks")
    print("3. Edit task")
    print("4. Remove task")
    print("5. Clear tasks")
    print("6. Quit")
    choice = (input("Please choose an option: "))
    if choice == "1":
            while True:
                print("\n1. Add task at a certain position")
                print("\n2. Add task anywhere")
                adding_choice = (input("Please select how to add your task: "))
                if adding_choice == "1":
                            if not tasks:
                                print("Your tasks is empty")
                            else:
                                for i, t in enumerate(tasks, start=1):
                                    print(f"{i}, {t}")
                                index = int(input("Enter the position you want to add the new task e.g 1,2,3... :"))
                                if 0 <= index <= len(tasks):
                                    add_choice = input("Enter the task to add: ")
                                    tasks.append(add_choice)               
                                    print("Task added successfully!")
                                    break
                elif adding_choice == 2:
                        task = input("Please enter a task: ")
                        tasks.append(task)
                        print("Task added to the bottom")
                break
    elif choice == "2":
        if not tasks:
            print("No Task yet!")
        else:
            print("\nYour tasks")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif choice == "3":
        if not tasks:
            print("No task to edit")
        else:
             for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
        index = int(input("Enter the task number you want to edit: "))
        if 1 <= index <= len(tasks):
            edited_task = input("Apply changes to selected task: ")
            tasks[index - 1] = edited_task
            print("Task apdated successfully!")
        else:
            print("Invalid task number")
    elif choice == "4":
        if not tasks:
            print("No task to remove")
        else:
            print("\nYour tasks")
            index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
           removed_task = tasks.pop(index - 1)
           print(f"Removed:  {removed_task}")
        else:
            print("Invalid task number")
    elif choice == "5":
                    while True:
                        if not tasks:
                             print("Your Task is empty")
                             break
                        print("Are you sure you want to clear all tasks?: ")            
                        print("1. Yes")
                        print("2. No")
                        choice_clear = input("Choose an option : ")
                        if choice_clear == "1":
                            tasks.clear()
                            print("All tasks cleared successfully!")
                            break
                        elif choice_clear == "2":
                             print("Canceled")
                             break
                        else:
                             print("Invalid option")
    elif choice == "6":
         # Save tasks to file before quitting
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")   
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")