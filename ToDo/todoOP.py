#For bonus, import json module
import json
from datetime import datetime

def addTodo(todo: str):
    '''
    This function takes todo as args and writes it to a file
    '''
    with open("ToDo/to_do.txt", "a+", encoding="utf-8") as file:
        #Store the list in a file
        file.write(f"{todo}\n")

def readTodo() -> str:
    '''
    This function retreives the to do list from the file then returns it
    '''
    todoList: list = []
    todoListFormatted:str = "Your To-Do list:\n"
    try:
        with open("ToDo/to_do.txt", "r", encoding="utf-8") as file:
        #Read from the file line by line and store in a list
            todoList = file.readlines()
    except FileNotFoundError:
        return "You To-Do list is empty."
    except Exception as e:
        return f"{e.__class__}"
    else:
        #Make sure list isn't empty
        if todoList != []:
            for i, todo in enumerate(todoList):
                todoListFormatted += f"{i + 1}. {todo}"
    
    return todoListFormatted

#--------------Bonus--------------
def addTodoBonus(todo: str, dateTime: str):
    '''
    This function takes todo as args and writes it to a file using json module
    '''
    todoList: dict = {}
    #Make sure the file exists to avoid errors
    try:
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList = json.load(file)
    except FileNotFoundError:
        return "Your To-Do list is empty."
    except Exception as e:
        return f"An error occured, {e.__class__}"
    finally:
        todoList[todo]= {
            'dateTime': dateTime,
            'done': False
        }
        with open("ToDo/to_do_bonus.json", "w", encoding="utf-8") as file:
            #Stores the todoList in a json file 
            json.dump(todoList, file, indent = 4)

def readTodoBonus() -> str:
    '''
    This function retreives the to do list from a json file, then returns a formatted string 
    containing all todo iteams and their details
    '''
    todoListFormatted:str = ""
    #Check that the file exists
    try:
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList: dict = json.load(file)
    except FileNotFoundError:
        return "Your To-Do list is empty."
    except Exception as e:
        return f"{e.__class__}"
    else:
        for i, todo in enumerate(todoList):
            todoListFormatted += f"{i + 1}. {todo} ({todoList[todo]['dateTime']}) - {'Done' if todoList[todo]['done'] else 'Not done'}\n"
        return todoListFormatted

def markAsDone(todo: str) -> str: 
    '''
    This function retreives To-Do list from a json file then marks a specific todo as done, then returns a message
    '''
    #Make sure the file exists to avoid errors
    try:
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList: dict = json.load(file)
    except FileNotFoundError:
        return "Your To-Do list is empty."
    except Exception as e:
        return f"{e.__class__}"
    else:
        #Make sure the todo is in the todoList dictionary
        if todo in todoList:
            #Make sure the todo isn't already done 
            if todoList[todo]['done'] is False:
                todoList[todo]['done'] = True
                with open("ToDo/to_do_bonus.json", "w", encoding="utf-8") as file:
                    #Stores the edited todoList in a json file 
                    json.dump(todoList, file, indent = 4)
                return f"'{todo}' has been marked as done"
            else:
                return f"'{todo}' is already done"
        else:
            return f"'{todo}' isn't on your To-Do list"

def searchByTitle(todo: str) -> str:
    '''
    This function takes a todo as args and returns its info
    '''
    todoInfo: str = ""
    #Make sure the file exists to avoid errors
    try:
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList: dict = json.load(file)
    except FileNotFoundError:
        return "Your To-Do list is empty."
    except Exception as e:
        return f"{e.__class__}"
    else:
        if todo in todoList:
            todoInfo = f"- {todo} ({todoList[todo]['dateTime']}) - {'Done' if todoList[todo]['done'] else 'Not done'}"
        else: 
            todoInfo = f"'{todo}' isn't on your To-Do list."

        return todoInfo
