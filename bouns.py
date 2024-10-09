from datetime import datetime
import os
import json


def to_do_list():
    
    while True:
        to_do_tasks = {}
        answer = input("do you want to add a new To-Do item? ")
        if answer.upper() == "Y":
            to_do= input("type your new to do item: ")
            title = to_do
            time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            

            
            try:
                with open("to_do.json", "r", encoding="UTF-8") as file:
                    to_do_tasks = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                to_do_tasks = {}
            to_do_tasks[title]={
                "title": title,
                "date and time": time,
                "done": False
            }
            with open("to_do.json", "w", encoding="UTF-8") as file:
                json.dump(to_do_tasks, file, indent=4)
        elif answer.upper() == "N":
            ans = input("do you want to list your To-Do items? ")
            if ans.upper() == "Y":
                try:
                    with open("to_do.json", "r", encoding="UTF-8") as file:
                        to_do_tasks = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    print("File is empty")
                
                for title, details in to_do_tasks.items():
                    print(f"- {details['title']} ({details['date and time']}) - {'DONE' if details['done'] else 'Not DONE'}")
                check = input("do you want to mark a specific task done? ")
                if check.upper() == "Y":
                    title= input("enter task name: ")
                    if title in to_do_tasks:
                        to_do_tasks[title]['done']= True
                        print("task is done")
                        with open("to_do.json", "w", encoding="UTF-8") as file:
                            json.dump(to_do_tasks, file)
                    else:
                        print("task not found")
                elif check.upper() == "N":
                    find = input("do you want to find a task by name? ")
                    if find.upper() == "Y":

                        title= input("enter task name you want to find: ")
                        if title in to_do_tasks:
                            
                            print(f"- {details['title']} ({details['date and time']}) - {'DONE' if details['done'] else 'Not DONE'}")
                        else:
                            print("task not found")
                    elif find.upper() == "EXIT":
                        print("thank you for using the To-Do program, come back again soon")
                        break
                    else:
                        to_do_list()
                elif check.upper() == "EXIT":
                    print("thank you for using the To-Do program, come back again soon")
                    break

                    
                else:
                    print("task not found")
            elif ans.upper() == "N":
                to_do_list()
            elif ans.upper() == "EXIT":
                print("thank you for using the To-Do program, come back again soon")
                break
        elif answer.upper() == "EXIT":
            print("thank you for using the To-Do program, come back again soon")
            break
        else:
            print("enter a valid answer (y or n)")
            to_do_list()

to_do_list()
    