import json
import datetime
todo_json={
    "task":[
        {
            "title":"task",
            "time":"time",
            "done":True
        }
    ]
}

file = open("to_do.json", "w", encoding="UTF-8")
try:
    json.dump(todo_json,file,indent=2)
except NameError as e:
    print(e)
    file.close()
except TypeError as e:
    print(e)
file.close()
file=open("to_do.json", "r", encoding="UTF-8")
try:
    content=json.load(file)
    print(f'{content["task"][0]["done"]}')
    file.close()
except IndentationError as e:
    print(e)
except Exception as e:
    print(e)
file.close()
def add_task(t1):
    file = open("to_do.json", "r", encoding="utf-8")

    tit = json.load(file)

    new_task={
        'title':t1,
        'time':datetime.datetime.today().isoformat(),
        'done':False
    }
    tit['task'].append(new_task)
    file = open("to_do.json", "w", encoding="utf-8")
    json.dump(tit,file,indent=2)
    print("it's added")
    return tit

def display_tasks():
    file_display = open("to_do.json", "r", encoding="utf-8")
    content_display=json.load(file_display)
    try:

        for task in content_display['task']:
            print(f'Task: {task["title"]} at: {task["time"]} done: {"done"if task["done"]else "not Done"}')
        file.close()
    except IndentationError as e:
        print(e)
    except Exception as e:
        print(e)

while True:
    tas=input("to you want add a task?y/n ")
    if tas=="y":
        ta1=input("what is it? ")
        add_task(ta1)
    elif tas=="n":
        qust=input("want to see your tasks?y/n ")
        if qust=="y":
            display_tasks()
        elif qust=="n":
            print("have a good day")
            input()
            break




file.close()
