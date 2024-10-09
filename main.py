from ToDo.todoOP import addTodo, readTodo, addTodoBonus, readTodoBonus, markAsDone, searchByTitle
import re

def main():
    '''
    Main function that contains all operations
    '''
    print("---Welcome to your To-Do List---")
    while True:
        print("Do you want to add a new To-Do item?")
        choice: str = input("Answer by 'y' for yes and 'n' for no and 'e' to exit: ")
        
        if choice.lower() == 'y':
            todo: str = input("Please write your To-Do item: ")
            addTodo(todo)

        elif choice.lower() == 'n':
            print("Do you want to list your To-Do item?")
            choice2: str = input("Answer by 'y' for yes and 'n' for no: ")
            if choice2.lower() == 'y':
                todoList = readTodo()
                print(todoList)
                input("")

            #If the user choses no it means they don't want to display the list nor add a new item,
            #so we break out of the loop
            elif choice2.lower() == 'n':
                break
            else:
                print("Invalid choice, please only enter 'y' for yes and 'n' for no.")
                input("")
        elif choice.lower() == 'e':
            print("Thank you for using the To-Do program, come again soon.")
            break
        else: 
            print("Invalid choice, please only enter 'y' for yes and 'n' for no.")
            input("")

#-----Bonus-----
def validateDatetime(date: str, time: str) -> str:
    '''
    This function validates date and time strings using regular expressions
    '''
    datePattern = "^[0-9]{1,2}\\-[0-9]{1,2}\\-[0-9]{4}$"
    timePattern = "^[0-5][0-9]\\:[0-5][0-9]$"
    if not re.match(datePattern, date):
        return "Invalid date format, only (dd-mm-yyyy) is allowed."
    elif not re.match(timePattern, time):
        return "Invalid time format, only (hh:mm) is allowed."
    else:
        return ""

def bonusMain():
    '''
    Main function for bonus solution operations
    '''
    print("---Welcome to your To-Do List---")
    while True:
        print("What would you like to do?")
        print("1. Add a new task.\n2. Mark a task as done.\n3. Search for a task by name.\n4. Display your To-Do list.\n5. Exit.")
        choice: str = input("Your choice: ")
        
        if choice == '1':
            todo: str = input("Please write your To-Do item: ")
            #Keep prompting user for correct date and time format
            while True:
                print("When do you want to do it? ")
                date: str = input("Date (dd-mm-yyyy): ")
                time: str = input("Time (hh:mm): ")
                errorMsg: str = validateDatetime(date, time)
                if errorMsg == "":
                    addTodoBonus(todo, date, time)
                    break
                else:
                    print(errorMsg)            
                
        elif choice == '2':
            todo: str = input("Please write the To-Do item you want to mark as done: ")
            msg = markAsDone(todo)
            print(msg)
            input("") 

        elif choice == '3':
            todo: str = input("Please write the To-Do item you want to search for: ")
            targetTodo: str = searchByTitle(todo)
            print(targetTodo)
            input("")

        elif choice == '4':
            print("Fetching your To-Do list..")
            todoList = readTodoBonus()
            print(todoList)
            input("")

        elif choice == '5':
            print("Thank you for using the To-Do list program, come again soon.")
            break
        else: 
            print("Invalid choice, try again.")
            input("")

#Execute main function
main()

#To execute bonus function remove comment
#bonusMain()
