import json
from datetime import datetime


def load_to_do():
    try:
        with open('to_do.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def dump_to_do(to_do):
    with open('to_do.json', 'w') as file:
        json.dump(to_do, file, indent=4)


def add_to_do():
    title = input("Enter your new To-Do item: ")
    todo_item = {
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }
    to_do.append(todo_item)
    dump_to_do(to_do)


def display_to_do():
    if not to_do:
        print("Your To-Do list is empty.")
    else:
        for index, todo in enumerate(to_do, start=1):
            status = "DONE" if todo["done"] else "NOT DONE"
            print(f"{index}. {todo['title']} ({todo['date']}) - {status}")


def mark_task_done():
    display_to_do()
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= index < len(to_do):
            to_do[index]["done"] = True
            dump_to_do(to_do)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def search_to_do():
    search_term = input("Enter the title to search: ")
    found = [todo for todo in to_do if search_term in todo["title"]]
    if found:
        for index, todo in enumerate(found, start=1):
            status = "DONE" if todo["done"] else "NOT DONE"
            print(f"{index}. {todo['title']} ({todo['date']}) - {status}")
    else:
        print("No tasks found with that title.")


to_do = load_to_do()

while True:
    user_input = input("Do you want to add a new To-Do item? (y/n/exit): ")

    if user_input == "y":
        add_to_do()
    elif user_input == "n":
        user_input = input("Do you want to list your To-Do items? (y/n): ")
        if user_input == "y":
            display_to_do()
            user_input = input("Do you want to mark a task as done? (y/n): ")
            if user_input == "y":
                mark_task_done()
            user_input = input("Do you want to search for a task? (y/n): ")
            if user_input == "y":
                search_to_do()
    elif user_input == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break
    else:
        print("Invalid input, please try again.")
