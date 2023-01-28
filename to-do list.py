import os

# Function to display the to-do list
def display_list():
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task.strip()}")

# Function to add a task to the to-do list
def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added.")

# Function to edit a task in the to-do list
def edit_task():
    display_list()
    task_number = int(input("Enter the number of the task to edit: "))
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    with open("tasks.txt", "w") as f:
        for i, task in enumerate(tasks):
            if i+1 == task_number:
                task = input(f"Edit task {task_number}: ")
                f.write(task + "\n")
                print("Task edited.")
            else:
                f.write(task)

# Function to delete a task from the to-do list
def delete_task():
    display_list()
    task_number = int(input("Enter the number of the task to delete: "))
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    with open("tasks.txt", "w") as f:
        for i, task in enumerate(tasks):
            if i+1 != task_number:
                f.write(task)
        print("Task deleted.")

# Main program loop
while True:
    print("\nTo-Do List")
    print("1. Display list")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display_list()
    elif choice == 2:
        add_task()
    elif choice == 3:
        edit_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
