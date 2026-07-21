# To Do List

tasks = []
running = True

while running:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Exit")

    if input == "1":
        print("Enter the task you would like to add")
        tasks.append(input)
    elif input == "2":
        print("these are the current tasks: " , \n tasks)

    elif input == "3":
        print("which task would you like to remove, enter a number: ")
        tasks.pop(input)
    elif input == "4":
        running = False
        print("exiting program...")
