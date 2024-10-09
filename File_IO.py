import os
import json

def to_Do():
    item_data = {}

    # Load existing data from the file if it exists
    if os.path.exists("to_do.txt"):
        with open("to_do.txt", "r", encoding="UTF-8") as file:
            try:
                item_data = json.load(file)
            except json.JSONDecodeError:
                item_data = {}

    while True:
        user_note = input("Do you want to add a new To-Do item? (y/n or 'exit' to finish): ").lower()
        if user_note == "exit":
            print("Thank you for using the To-Do program, come back again soon!")
            break
        
        if user_note == "y":
            title = input("Enter the title of your To-Do item: ")
            date_time = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            done = False

            # Check if the task already exists to avoid duplicates
            if title not in item_data:
                # Store the new to-do item
                item_data[title] = {
                    'date_time': date_time,
                    'done': done
                }

                # Save the updated list to the file
                with open("to_do.txt", "w", encoding="UTF-8") as file:
                    json.dump(item_data, file, indent=4)
                print(f"Added new task: {title}")
            else:
                print(f"The task '{title}' already exists.")

        elif user_note == "n":
            list_items = input("Do you want to list your To-Do items? (y/n): ").lower()
            if list_items == "y":
                # Read and display the to-do items
                if item_data:
                    for i, (title, details) in enumerate(item_data.items(), start=1):
                        status = "DONE" if details['done'] else "NOT DONE"
                        print(f"{i}. {title} ({details['date_time']}) - {status}")
                else:
                    print("No items found.")

            mark_done = input("Do you want to mark an item as done? (y/n): ").lower()
            if mark_done == "y":
                task_to_mark = input("Enter the title of the task to mark as done: ")
                if task_to_mark in item_data:
                    item_data[task_to_mark]['done'] = True
                    print(f"Task '{task_to_mark}' marked as DONE.")

                    # Save the updated list to the file
                    with open("to_do.txt", "w", encoding="UTF-8") as file:
                        json.dump(item_data, file, indent=4)
                else:
                    print("Task not found.")

    return item_data

to_Do()
