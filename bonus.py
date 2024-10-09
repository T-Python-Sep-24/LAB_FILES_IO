
import json
list_dict=[]

while True:
    user_choice=input("do you want to add a new To-Do item? (Y)->yes, (N)->no or (exit): ")
    #End program
    if user_choice.upper() == "EXIT":
        print("thank you for using the To-Do program, come back again soon")
        break
    #Add items
    if user_choice.upper() == "Y":
        u_contentTitle= input("write your To-Do item: ")
        u_contentDate= input("write date & time as (YYYY-MM-DD HH:MM:SS): ")
        u_contentDone= input("write if you done this task or not (D)->done: ")
               
        if u_contentDone.upper()=="D":
            user_task={
            "title":u_contentTitle,
            "dateTime":u_contentDate,
            "doneOrnot":True
            }
            list_dict.append(user_task)
        else:
            user_task={
            "title":u_contentTitle,
            "dateTime":u_contentDate,
            "doneOrnot":False
            }
            list_dict.append(user_task)          

    #Display items
    elif user_choice.upper() == "N": 
        user_2choice=input("do you want to list your To-Do items ? (Y)->yes, (N)->no: ")
        file= open("to_do.json","w",encoding="UTF-8")
        json.dump(list_dict,file)
        file.close()

        if user_2choice.upper() == "Y":
            with open("to_do.json", "r",encoding="utf-8") as file:
                        json_string = file.read()
                        content = json.loads(json_string)
                        for index,item in enumerate(content, start=1):
                         print(f"{index}. {item["title"]} ({item["dateTime"]}) - {'DONE' if item["doneOrnot"] else 'NOT DONE'}") 
  
        elif user_2choice.upper() == "N":
          user_3choice=input("Mark a task as Done (D) - Search a task (S): ")
        
        #Done function
          if user_3choice.upper()=="D":
              theTask=input("Enter the title of task you want to marked as DONE: ")
              for item in list_dict:
                  if theTask in item["title"]:
                      item["doneOrnot"]=True
              print()
              file= open("to_do.json","w",encoding="UTF-8")
              json.dump(list_dict,file)
              file.close()
              with open("to_do.json", "r",encoding="utf-8") as file:
                    json_string = file.read()
                    content = json.loads(json_string)
                    for index,item in enumerate(content, start=1):
                         print(f"{index}. {item["title"]} ({item["dateTime"]}) - {'DONE' if item["doneOrnot"] else 'NOT DONE'}") 

        #Search function
          elif user_3choice.upper() == "S":
            theTask = input("Enter the title of the task you want to search: ")
            task_found = False

            for index,item in enumerate(list_dict,start=1):
                if theTask in item["title"]:
                    print()
                    print(f"{index}. {item['title']} ({item['dateTime']}) - {'DONE' if item['doneOrnot'] else 'NOT DONE'}")
                    task_found = True
                    print() 
                    print("IT IS FOUND")

            if not task_found:
                print("No task found with that title.")

    # handle with unwanted inputs    
    else:
        print('you entered invalid charachter, Try again.')  
        