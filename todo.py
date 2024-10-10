def load_todo_list():
    try:
        with open('to_do.txt', 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_todo_item(item):
    with open('to_do.txt', 'a') as file:
        file.write(item + '\n')

def main():
    while True:
        user_input = input("Do you want to add new To-Do item? (y/n or type 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            print("Thank you for using the To-Do program, come back again soon !")
            break
        elif user_input == 'y':
            todo_item = input("Enter your new To-Do item: ")
            save_todo_item(todo_item)
            print("To-Do item added!")
        elif user_input == 'n':
            user_input = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
            if user_input == 'y':
                todo_list = load_todo_list()
                if not todo_list:
                    print("Your To-Do list is empty.")
                else:
                    print("Your To-Do items:")
                    for item in todo_list:
                        print(f"- {item}")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()