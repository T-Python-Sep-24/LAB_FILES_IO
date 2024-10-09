while True:
    print("Do you want to add a new To-Do item?")
    pick: str = input("'y' for yes and 'n' for no: ")

    if pick == "y":
        # ask the user to type in his new To-Do item . 
        toDo_item = input("type in a new To-Do item: ")
        # save that To-Do item inside the a file to_do.txt on a new line.
        with open("to_do.txt", "a+", encoding="UTF-8") as file:
            file.write(f"{toDo_item}\n")
            
        print("++++ To-do item was successfully added ++++\n")
    elif pick == "n":
        # ask the user : do you want to list your To-Do items ?
        print("\ndo you want to list your To-Do items ?")
        pick: str = input("'y' for yes and 'n' for no: ")

        #if the user answers yes. Print a list of the To-Do items
        if pick == "y":
            try:
                with open("to_do.txt", "r", encoding="UTF-8") as file:
                    fileLines: list[str] = file.readlines()

                    print(f"\n**** To-Do List ****")
                    for line in fileLines:
                        print(f"- {line}", end="")
                input("")
            except FileNotFoundError:
                print("You don't have any Tasks")
                input("")
            except Exception as e:
                print("Something went wrong... {e}")
                input("")
        elif pick == "n":
            print("")
        else:
            print("==== Wrong input ====")
            input("")
    # exit of the program if user type exit
    elif pick == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break
    else:
        print("==== Wrong input ====")
        input("")


