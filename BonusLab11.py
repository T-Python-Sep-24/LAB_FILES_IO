#Bonus Lab 11
import json
import datetime

def todo_jason(todo_r_filename = "To-Do.json"):
    try:
        with open(todo_r_filename, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    


def save_todo_jason(todo, todo_w_filename = "To-Do.json"):
    with open(todo_w_filename, "w") as file:
        json.dump(todo, file, indent=4)



def add_todo(todo: list, title: str, dateandtime: str):
    new_todo = {
        "Title": title,
        "Date and Time": dateandtime,
        "Done": False
    }
    todo.append(new_todo)
    print(f"{title} ({dateandtime}) is added successfully.")
    save_todo_jason(todo)



def display_todo(todo: list):
    print("Your To-Do List is:")
    for num, item in enumerate(todo, 1):
        done_status = "Done" if item['Done'] else "Not Done"
        print(f"{num}. {item['Title']} ({item['Date and Time']}) - {done_status}")



def mark_todo(todo: list, title: str):
    for item in todo:
        if item['Title'].lower() == title.lower():
            item['Done'] = True
            print(f"{title} has been marked as done.")
            save_todo_jason(todo)
            return
    print("Task not found")



def search_todo(todo: list, title: str):
    print("Search Results:")
    found = False
    for num, item in enumerate(todo, 1):
        if title.lower() in item['Title'].lower():
            done_status = "Done" if item['Done'] else "Not Done"
            print(f"{num}. {item['Title']} ({item['Date and Time']}) - {done_status}")
            found = True
    if not found:
        print("No matching tasks found.")



def main():
    print("Welcome to Our Program")
    print("*" * 20)
    todo = todo_jason()

    while True:
        user_todo = input("\nPlease Choose an Option:\n1. Add a New Item\n2. Display Your Items\n3. Mark an Item as Done\n4. Search Items\n5. Exit\nYour Option is: ")
        
        if user_todo == "1":
            title = input("Enter the title of the task: ")
            dateandtime = input("Enter the date & time (YYYY-MM-DD HH:MM:SS): ")
            add_todo(todo, title, dateandtime)
        
        elif user_todo == "2":
            display_todo(todo)
        
        elif user_todo == "3":
            title = input("Enter the title of the task to mark as done: ")
            mark_todo(todo, title)
        
        elif user_todo == "4":
            title = input("Enter the title to search: ")
            search_todo(todo, title)
        
        elif user_todo == "5":
            print("Thank you for using the To-Do Program. Come back soon!")
            break
        
        else:
            print("This option is not in the list. Please try again.")

if __name__ == "__main__":
    main()


