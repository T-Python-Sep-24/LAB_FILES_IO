'''
## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , 
# this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . 
Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" ,
 then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''
import os 
def add_todo():
    try:
        with open('to_do.txt','a',encoding="UTF-8") as file:
                to_do=input("\nWrite your to-do item: " ).strip()
                file.write(to_do+"\n")
    except Exception as e:
           print(e.__class__)
def get_todo_list():
    try:
        with open('to_do.txt','r',encoding="UTF-8")as file:
                content=file.read()
                if   content:
                        print('\n'+content)
                        input("press any key to continue")
                else:
                    print("there is nothing in your todo_list\n")
                    input("press any key to continue")
                   
    except FileNotFoundError as e:
           print("There is no such file in Your working directory.")
           print(os.getcwd())
while True:
        Choice=input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no.\npress e to exit: ').lower()
        print()
        if Choice=='y':
                add_todo()
        elif Choice=='n':
                Choice=input('do you want to list your To-Do items ? answer "y" for yes and "n" for no. ').lower()
                print()
                if Choice=='y':
                        get_todo_list()
                elif Choice=='n':
                        print()
                else:
                        print("Invalid input!")
        elif Choice=='e':
            break     
        else:
                print("invalid input")
                