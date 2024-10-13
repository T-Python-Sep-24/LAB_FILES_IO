import json
from datetime import datetime

def addTask(tasksDict: dict):
    ''' add task to JSON file'''
    print("\n---------- Adding a Task ----------")
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
    # add the new data to the dict using title as key
    tasksDict[item_title] = newTask


def listTasks(tasksDict):
    ''' asks if user wants to list his To-Do items '''
    print("\n---------- Listing the Tasks ----------")

    # check if there is existing data or print aproprite message
    if len(tasksDict) > 0:
        for index, (title, task) in enumerate(tasksDict.items(), start=1):
                if not task['item_done']:
                    item_status:str = "Not Done"
                else:
                    item_status:str = "Done"
                    
                print(f"{index}. {title} ({task['item_dateTime']}) - {item_status}")
        input("")
    else:
        pass
        print("You don't have any Tasks")
        input("")


def markTask(tasksDict):
    ''' mark a specific task as done '''
    print("\n---------- Marking a Task as Done ----------")
    item_title = input("Type a task title to mark it as done: ")

    if item_title in tasksDict.keys():
        # change task to done if not alreadey
        if tasksDict[item_title]["item_done"] == False:
            tasksDict[item_title]["item_done"] = True
            print("++++++++++ The task marked as done successfully ++++++++++\n")
            input("")
        else:
            print("The task already marked as done")
            input("")
    else:
        print("The title doesn't exist")
        input("")


def searchTasks(tasksDict):
    ''' search a specific task by title '''
    print("\n---------- Searching a Task by Title ----------")
    item_title = input("Type a task title to search for: ")

    # if the task exist show it
    if item_title in tasksDict.keys():
        print("Task is found: ")
        task = tasksDict[item_title]
        if not task['item_done']:
            item_status:str = "Not Done"
        else:
            item_status:str = "Done"
        print(f"- {item_title} ({task['item_dateTime']}) - {item_status}")
        print("++++++++++ Searching a task completed successfully ++++++++++\n")
        input("")
    else:
        print("Task is not found")
        input("")        
        