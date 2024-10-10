while True:
    ask_user = input("Do you want to add a new To-Do item? (y/n or type 'exit' to quit): ")

    if ask_user == "y":
        todo_item = input("Type in your new To-Do item: ")

        with open("to_do.txt", "a+", encoding="UTF8") as file:
            file.write(todo_item + "\n")
        print(f'Added "{todo_item}" to your To-Do list.')

    elif ask_user == "n":
        list_items = input("Do you want to list your To-Do items? Answer 'y' for yes and 'n' for no: ")

        if list_items == "y":
            with open("to_do.txt", "r", encoding="UTF8") as file:
                items = file.readlines()
                if items:
                    print("Here is your To-Do list:")
                    for idx, item in enumerate(items, start=1):
                        print(f"{idx}. {item.strip()}")
                else:
                    print("Your To-Do list is currently empty.")

    elif ask_user == "exit":
        print("Thank you for using the To-Do program. Come back again soon!")
        break

    else:
        print("Invalid input, please enter 'y', 'n', or 'exit'.")

