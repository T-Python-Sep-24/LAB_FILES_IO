

while True:
    user_choice=input("do you want to add a new To-Do item? (Y)->yes, (N)->no or (exit): ")
   
    if user_choice.upper() == "EXIT":
        print("thank you for using the To-Do program, come back again soon")
        break

    if user_choice.upper() == "Y":
        user_content= input("write your To-Do item: ")
        file= open("to_do.txt","a",encoding="UTF-8")
        file.write("- "+user_content+"\n")
        file.close()
 
    elif user_choice.upper() == "N": 
        user_2choice=input("do you want to list your To-Do items ? (Y)->yes, (N)->no: ")
 
        if user_2choice.upper() == "Y":
            with open("to_do.txt", encoding="utf-8") as file:
                content=file.read()
                print(content)
  
        elif user_2choice.upper() == "N":
            print("thank you for using the To-Do program, come back again soon")   
            break
        
    else:
        print('you entered invalid charachter, Try again.')
          
        