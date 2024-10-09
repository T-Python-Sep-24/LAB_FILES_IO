def main():
    while True:
        #Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
        #Using the methods strip() and lower() to ensure that the user's input is correct 
        #without considering the spaces and the upper/lowerCase 
        add_todo = input("Do you want to add a new To-Do item? (y/n): ").strip().lower()
        
        #If the user answers yes , then ask the user to type in his new To-Do item . 
        #Then save that To-Do item inside the a file to_do.txt on a new line.
        if add_todo == 'y':
            todo_item = input("Please type in your new To-Do item: ")
            #Open the file to_do.txt in append mode ('a'). 
            #Any new content will be added to the end of the file without deleting its existing content.
            with open('to_do.txt', 'a') as file:
                file.write(todo_item + '\n')
        
        #If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
        elif add_todo == 'n':
            list_todos = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
            if list_todos == 'y':
                
                #Using try and except to prevent the errors that might be occure while trying to open the file 
                try:
                    with open('to_do.txt', 'r') as file:
                        todos = file.readlines()
                        print("Your To-Do List:")
                        for item in todos:
                            print(item.strip())
                except FileNotFoundError:
                    print("No To-Do items found. Please add some first.")
        
        else:
            print("Invalid input. Please answer with 'y' or 'n'.")
        
        exit_program = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
        if exit_program == 'exit':
            print("Thank you for using the To-Do program, come back again soon!")
            break

if __name__ == "__main__":
    main()
