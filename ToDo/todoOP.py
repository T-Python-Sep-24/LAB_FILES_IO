#For bonus, import json module
import json
from os import path

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
    todoListFormatted:str = "Your To-Do list:\n"
    with open("ToDo/to_do.txt", "r", encoding="utf-8") as file:
        #Read from the file line by line and store in a list
        todoList: list = file.readlines()
        #Make sure list isn't empty
        if todoList != []:
            for i, todo in enumerate(todoList):
                todoListFormatted += f"{i + 1}. {todo}"
    
    return todoListFormatted

#--------------Bonus--------------
def addTodoBonus(todo: str, date: str, time: str):
    '''
    This function takes todo as args and writes it to a file using json module
    '''
    todoList: dict = {}
    #Make sure the file exists to avoid errors
    if path.isfile("ToDo/to_do_bonus.json"):
        #Load the existing data from the json file if it exists
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            todoList = json.load(file)

    todoList[todo]= {
        'date': date,
        'time': time,
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
    if path.isfile("ToDo/to_do_bonus.json"):
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList: dict = json.load(file)
        for i, todo in enumerate(todoList):
            todoListFormatted += f"{i + 1}. {todo} ({todoList[todo]['date']} {todoList[todo]['time']}) - {'Done' if todoList[todo]['done'] else 'Not done'}\n"
        return todoListFormatted
    else:
        return "Your To-Do list is empty."

def markAsDone(todo: str) -> str: 
    '''
    This function retreives To-Do list from a json file then marks a specific todo as done, then returns a message
    '''
    #Make sure the file exists to avoid errors
    if path.isfile("ToDo/to_do_bonus.json"):
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList: dict = json.load(file)
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
    else:
        return "Your To-Do list is empty."

def searchByTitle(todo: str) -> str:
    '''
    This function takes a todo as args and returns its info
    '''
    todoInfo: str = ""
    #Make sure the file exists to avoid errors
    if path.isfile("ToDo/to_do_bonus.json"):
        with open("ToDo/to_do_bonus.json", "r", encoding="utf-8") as file:
            #Get the information from the json file by using .load() function
            todoList: dict = json.load(file)
        if todo in todoList:
            todoInfo = f"- {todo} ({todoList[todo]['date']} {todoList[todo]['time']}) - {'Done' if todoList[todo]['done'] else 'Not done'}"
        else: 
            todoInfo = f"'{todo}' isn't on your To-Do list."

        return todoInfo
    else:
        return "Your To-Do list is empty."
