import json
import os
from datetime import datetime

def read_file():
        try:
            with open('Todo_list.json','r',encoding="UTF-8")as file:
             todo_list=json.load(file)
             return todo_list
        except Exception as e:
            print(e.__class__)

def save_file(items:list):
    with open('Todo_list.json','w',encoding="UTF-8")as file:
        json.dump(items,file,indent=4)


        
def add_todo_item():
    if os.path.exists('Todo_list.json') and os.path.getsize("Todo_list.json")>0:
        todo_list=read_file()
    else:
        todo_list=[]
    todo=input("Enter Todo item:").strip()
    date=str(datetime.now())
    status=False
    item={
        'title':todo,
        'date':date,
        'status':status
        }
    todo_list.append(item)
    save_file(todo_list)
   
def show_todolist():
            if os.path.exists('Todo_list.json') and os.path.getsize("Todo_list.json")>0:
                todo_list=read_file()
            else:
                print("There is nothing in your Todolist")
                return
            if todo_list:
                for index,todo in enumerate(todo_list,start=1):  
                    status="Done" if todo['status']else"Not Done"
                    print(f"{index}. {todo['title']} ({todo['date']}) - {status}")
            else:
                print("there is no tasks in your list")
              
                
    

def mark_done():
    if os.path.exists('Todo_list.json') and os.path.getsize("Todo_list.json")>0: 
        todo_list=read_file()
        todo=input("what is the name of the task that you done!: ").strip()
    else:
        print("There is nothing in your Todolist")
        return
    for task in todo_list:
        if task['title']==todo:
                task['status']=True
                save_file(todo_list)
                break
    else:
        print("There is no task with this name!")

def get_specfic_todo_item():
    if os.path.exists('Todo_list.json') and os.path.getsize("Todo_list.json")>0:
        todo_list=read_file()
        todo=input("what is the name of the task You want to see!: ").strip()
    else:
        print("There is nothing in your Todolist")
        return
    for task in todo_list:
         if task['title']==todo:
              status="Done" if task['status']else"Not Done"
              print(f"{task['title']} ({task['date']}) - {status}")
              return
    else:
        print("there is no task with that name!")
def main():
    print("Welcome To task manager!")
    while True:
        print("\n1-Add task\n2-show tasks\n3-check task\n4-search specfic task\n5-exit")
        choice=input("choose: ")
        if choice=='1':
            add_todo_item()
            input("press any key to continue")
        elif choice=='2':
            show_todolist()
            input("press any key to continue")
        elif choice=='3':
            mark_done()
            input("press any key to continue")
        elif choice=='4': 
            get_specfic_todo_item()
            input("press any key to continue")
        elif choice=='5':
            break
        else:
            print("Invalid input")
main()