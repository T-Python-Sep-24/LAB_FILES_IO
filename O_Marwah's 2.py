def todo_manager():
    filename = 'to_do.txt'

    while True:
        user_choice = input("Do you want to add a new To-Do item? (y/n/exit): ").strip().lower()
        
        if user_choice == 'y':
            selected_item = input("Start to type your tasks To-Do item: ").strip()
            with open(filename, 'a') as file:
                file.write( selected_item + '\n')
            print("To-Do item added.")

        elif user_choice == 'n':
            list_task = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
            if list_task == 'y':
                try:
                    with open(filename, 'r') as file:
                        todos = file.readlines()
                        if todos:
                            print("Your To-Do List:")
                            for item in todos:
                                print("- " + item.strip())
                        else:
                            print("Your To-Do list is empty.")
                except FileNotFoundError:
                    print("No tasks found yet.")

        elif user_choice == 'exit':
            print("Thank you for using the To-Do program, come back again soon.")
            break
        
        else:
            print("wrong input. Please enter 'y', 'n', or 'exit'.")

if __name__ == "__main__":
    todo_manager()




