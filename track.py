import os

def load_list(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().splitlines()
    else:
        return []

def save_list(filename, items):
    with open(filename, 'w') as file:
        file.write("\n".join(items))

def add_item(items, item):
    items.append(item)
    print("Item added.")

def remove_item(items, item):
    if item in items:
        items.remove(item)
        print("Item removed.")
    else:
        print("Item not on list.")

def view_list(items):
    if items:
        for i, item in enumerate(items):
            print(i+1, item)
    else:
        print("Shopping list is empty.")

# Get file name
filename = input("Enter the name of the file to save and load the list: ")

# Load the list from the file
items = load_list(filename)

while True:
    # Get user input
    action = input("Enter 'view', 'add', 'remove', 'save', or 'exit': ").lower()

    # Perform action based on user input
    if action == 'view':
        view_list(items)
    elif action == 'add':
        item = input("Enter item to add: ")
        add_item(items, item)
    elif action == 'remove':
        item = input("Enter item to remove: ")
        remove_item(items, item)
    elif action == 'save':
        save_list(filename, items)
        print("List saved.")
    elif action == 'exit':
        break
    else:
        print("Invalid action.")
