# Mini Project 2 — To-Do List Manager

tasks = []  # Empty list to store tasks

while True:
    # Print menu
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    # Option 1 — Add a task
    if choice == "1":
        new_task = input("Enter the task to add: ")
        tasks.append(new_task)
        print(f'"{new_task}" has been added.')
    
    # Option 2 — Remove a task
    elif choice == "2":
        task_to_remove = input("Enter the task to remove: ")
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print(f'"{task_to_remove}" has been removed.')
        else:
            print(f'"{task_to_remove}" not found in your tasks.')
    
    # Option 3 — Show all tasks
    elif choice == "3":
        if tasks:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks in the list.")
    
    # Option 4 — Exit
    elif choice == "4":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    
    # Invalid input
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")



