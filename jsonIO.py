import json
import datetime
import os

import json
import datetime
import os

def add_task_to_file(task: str):
    """
    Adds a new task to the to-do list JSON file.
    """
    file_path = "to_do.json"

    if not os.path.exists(file_path):
        file =  open("to_do.json", 'w', encoding='utf-8')
        json.dump([], file)

    file =  open("to_do.json", 'r', encoding='utf-8')
    if os.path.getsize(file_path):
        tasks = json.load(file)
    else:
        tasks = []

    # make new task
    new_task = {
        "title": task,
        "dateTime": str(datetime.datetime.now()),
        "Done": False
    }
    tasks.append(new_task)
    json_file = open("to_do.json", 'w', encoding='utf-8')
    json.dump(tasks, json_file, indent=4)

    return "Task added successfully"


def mark_task_as_done(task_num: int):
    """
    function to modify task as done based on the task number the user chooses.
    """
    file_path = "to_do.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("No tasks found.")
        return

    # Load existing tasks
    file = open("to_do.json", 'r', encoding='utf-8')
    tasks = json.load(file)

    if task_num <= len(tasks) and task_num >= 0:
        tasks[task_num - 1]["Done"] = True
        tasksFile = open("to_do.json", 'w', encoding='utf-8')
        json.dump(tasks, tasksFile, indent=4)
        print(f"Task {task_num} marked as done.")
    else:
        print("Wrong task number. please try a valid number")


def search_tasks(keyword: str):
    """
    Searches for tasks that contain the given keyword.
    """
    file_path = "to_do.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("No tasks found.")
        return

    # Load existing tasks
    file = open("to_do.json", 'r', encoding='utf-8')
    tasks = json.load(file)

    print(f"Search results for '{keyword}':")
    found = False
    for i, task in enumerate(tasks, start=1):
        if keyword.lower() in task["title"].lower():
            format_output(i, task)
            found = True

    if not found:
        print(f"No tasks found with the keyword '{keyword}'.")


def format_output(index, task):
    """
    Formats and prints a task from the to-do list.
    """
    print(f"{index}. {task['title']} ({task['dateTime']}) - {'Done' if task['Done'] else 'Not Done'}")


def print_tasks():
    """
    Reads and prints all tasks from the to-do list.
    """
    file_path = "to_do.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("No tasks found.")
        return

    # Load tasks
    file = open("to_do.json", 'r', encoding='utf-8')
    tasks = json.load(file)

    # Print tasks
    print("--------------- Your To-Do List ---------------")
    for i, task in enumerate(tasks, start=1):
        format_output(i, task)
    print("-----------------------------------------------")


# the main function
def main():
    while True:

        print("---------- To Do List App ----------")
        user_input = input("1. Add a Task\n2. Show To-Do List\n3. Mark Task as Done\n4. Search for a Task\n[exit] to quit application\n")

        if user_input.lower() == "exit":

            print("Thank you for using the To-Do program. Come again soon!")
            break

        elif user_input == "1":

            user_task = input("Enter Your Task: ")
            print(add_task_to_file(user_task))
            input(" >> Press Any Button to Continue << ")

        elif user_input == "2":

            print_tasks()
            input(" >> Press Any Button to Continue << ")

        elif user_input == "3":

            print_tasks()
            task_num = int(input("Enter the task number to mark as done: "))
            mark_task_as_done(int(task_num))
            input(" >> Press Any Button to Continue << ")

        elif user_input == "4":

            keyword = input("Enter a keyword to search for relevant tasks: ")
            search_tasks(keyword)
            input(" >> Press Any Button to Continue << ")

        else:

            print("Invalid input, please try again.")
            input(" >> Press Any Button to Continue << ")

try:
    main()
except ValueError:
    print("Invalid Input, try with valid input")