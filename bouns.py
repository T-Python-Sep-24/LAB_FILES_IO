from datetime import datetime
import json
import os

to_do_tasks = {}


def save_data(): #Function to save data to a JSON file
    with open("to_do.json", "w", encoding="UTF-8") as file:
        json.dump(to_do_tasks, file, indent=4)


def load_data():# Function to load data from a JSON file
    global to_do_tasks
    try:
        with open("to_do.json", "r", encoding="UTF-8") as file:
            to_do_tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        to_do_tasks = {}


def to_do_list():# Main to-do list function
    load_data()
    
    while True:
        answer = input("Do you want to add a new To-Do item? ")

        if answer.upper() == "Y":# add to do tasks
            to_do = input("Type your new To-Do item: ")
            title = to_do
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            done = False

            
            to_do_tasks[title] = {
                "title": title,
                "date and time": time,
                "done": done
            }
            save_data()
            print(f"to do task: '{title}' has been added.")
        
        elif answer.upper() == "N":
            list_choice = input("Do you want to list your To-Do items? ")
            if list_choice.upper() == "Y":#list to do tasks
                
                for index, (title, details) in enumerate(to_do_tasks.items(), start=1):
                        print(f"{index}. {details['title']} ({details['date and time']}) - {'DONE' if details['done'] else 'Not DONE'}")
                        is_done = input("Mark this task as done? ")
                        if is_done.upper() == "Y":#mark tasks done
                            to_do_tasks[title]["done"] = True
                            save_data()
                            print(f"to do task '{title}' marked as DONE.")
            
            elif list_choice == "EXIT":
                print("Thank you for using the To-Do program. Come back again soon.")
                break

            elif list_choice.upper() == "N":
                find = input("Do you want to find a task by name? ")

                if find.upper() == "Y":#find task by name
                    title = input("Enter the task name you want to find: ")
                    if title in to_do_tasks:
                        details = to_do_tasks[title]
                        print(f"- {details['title']} ({details['date and time']}) - {'DONE' if details['done'] else 'Not DONE'}")
                    else:
                        print("Task not found.")
                
                elif find.upper() == "EXIT":
                    print("Thank you for using the To-Do program. Come back again soon.")
                    break

        elif answer.upper() == "EXIT":
            print("Thank you for using the To-Do program. Come back again soon.")
            break

        else:
            print("Invalid input. Please enter Y, N, or EXIT.")
            continue

to_do_list()
