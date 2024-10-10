import os
def to_do_list():
    while True:
        answer = input("do you want to add a new To-Do item? ")
        if answer.upper() == "Y":
            to_do= input("type your new to do item: ")
            file = open("to_do.txt", "a", encoding="UTF-8")
            file.write(to_do + "\n")
            file.close()
        elif answer.upper() == "N":
            ans = input("do you want to list your To-Do items? ")
            if ans.upper() == "Y":
                file = open("to_do.txt", "r", encoding="UTF-8")
                file.seek(0)
                print(file.read())
                file.close()
            elif ans.upper() == "N":
                to_do_list()
            elif ans.upper() == "EXIT":
                print("thank you for using the To-Do program, come back again soon")
                break
        elif answer.upper() == "EXIT":
            print("thank you for using the To-Do program, come back again soon")
            break
        else:
            print("enter a valid answer (y or n)")
            to_do_list()

to_do_list()
    