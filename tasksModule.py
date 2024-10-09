import json
from datetime import datetime

def addTask():
    ''' add task to JSON file'''
    print("\n---------- Adding a Task ----------")
    # check if there is existing data pull it or create new dict
    try:
        with open("to_do.json", "r") as file:
            existingData: dict = json.load(file)
    except FileNotFoundError:
        existingData = {}


    # ask the user to type in his new To-Do item . 
    item_title: str = input("Type in a new To-Do item: ")
    # creat a dict for the item
    item_done: bool = False
    currentDateTime: datetime = datetime.now()
    item_dateTime: str = currentDateTime.strftime("%Y-%m-%d %H:%M:%S")
    
    newTask: dict = {
        "item_done": item_done,
        "item_dateTime": item_dateTime 
    }
    # add new data to the existing dict using title as key
    existingData[item_title] = newTask

    # save that To-Do item inside the a file to_do.json
    with open("to_do.json", "w") as file:
        json.dump(existingData, file, indent = 4)
    print("++++++++++ To-do item was successfully added ++++++++++\n")


def listTasks():
    ''' asks if user wants to list his To-Do items '''
    print("\n---------- Listing the Tasks ----------")
    # check if there is existing data or print aproprite message
    try:
        with open("to_do.json", "r") as file:
            tasks: dict = json.load(file)

            for index, (title, task) in enumerate(tasks.items(), start=1):
                if not task['item_done']:
                    item_status:str = "Not Done"
                else:
                    item_status:str = "Done"
                    
                print(f"{index}. {title} ({task['item_dateTime']}) - {item_status}")
        input("")
    except FileNotFoundError as e:
        print("You don't have any Tasks")
        input("")
    except Exception as e:
        print("Something went wrong... {e}")
        input("")


def markTask():
    ''' mark a specific task as done '''
    print("\n---------- Marking a Task as Done ----------")

    item_title = input("Type a task title to mark it as done: ")

    # check if there is existing data pull it or create new dict
    try:
        with open("to_do.json", "r") as file:
            existingData: dict = json.load(file)
    except FileNotFoundError:
        print("You don't have any Tasks")
    except Exception as e:
        print("Something went wrong... {e}")
        input("")

    if item_title in existingData.keys():
        # change task to done if not alreadey
        if existingData[item_title]["item_done"] == False:
            existingData[item_title]["item_done"] = True
            # update json file
            with open("to_do.json", "w") as file:
                json.dump(existingData, file, indent = 4)
            print("++++++++++ The task marked as done successfully ++++++++++\n")
            input("")
        else:
            pass
            print("The task already marked as done")
            input("")
    else:
        print("The title doesn't exist")
        input("")

def searchTasks():
    ''' search a specific task by title '''
    print("\n---------- Searching a Task by Title ----------")

    item_title = input("Type a task title to search for: ")

    # check if there is existing data show the task
    try:
        with open("to_do.json", "r") as file:
            existingData: dict = json.load(file)
            if item_title in existingData.keys():
                # change task to done
                print("Task is found: ")
                task = existingData[item_title]
                if not task['item_done']:
                    item_status:str = "Not Done"
                else:
                    item_status:str = "Done"
                print(f"- {item_title} ({task['item_dateTime']}) - {item_status}")
                print("++++++++++ Searching a task completed successfully ++++++++++\n")
                input("")

    except FileNotFoundError:
        print("You don't have any Tasks")
        input("")
    except Exception as e:
        print(f"Something went wrong... {e}")
