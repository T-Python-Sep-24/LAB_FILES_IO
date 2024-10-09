import json

todos = []

while True:
    options = input("Do you want to add a new To-Do item? (Y/N): ")
    if options.upper() == 'Y':
        title = input("Enter the title of the To-Do: ")
        date = input("Enter the date: ")
        time = input("Enter the time: ")

        todos.append({
            "title": title,
            "date": date,
            "time": time,
            "done": False
        })

        with open("todo.txt", "a+", encoding="utf-8") as file:
            file.write(f"{title},{date},{time},False\n")

    elif options.upper() == 'N':
        view = input("Do you want to list your To-Do items? (Y/N): ")
        if view.upper() == 'Y':
            print("Your To-Do list:")
            for index, todo in enumerate(todos, start=1):
                status = "DONE" if todo["done"] else "NOT DONE"
                print(f"{index}. {todo['title']} ({todo['date']} {todo['time']}) - {status}")
        else:
            break

    elif options.lower() == "exit":
        break