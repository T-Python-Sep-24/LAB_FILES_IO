#Lab 11

print("Welcome to Our Program")
print("*" * 20)

while True:
    user_todo = input ("Do You Want to Add a New Item to Your To-Do List ? Type 'y' to 'Yes' and 'n' to 'No'")
    if user_todo == "Exit":
        print("Thank You for Using the To-Do Program, Come Back Again Soon")
        break

    elif user_todo == "y":
        user_say_yes = input("Please Enter Your Item:") 
        file = open("to_do.txt", "a", encoding="UTF-8")
        file.write (user_say_yes + "\n")
        file.close()

    elif user_todo == "n":
        user_say_no = input("Do You Want to Read Your To-Do List ? Type 'y' to 'Yes' and 'n' to 'No'")
        if user_say_no == "y":
            file = open("to_do.txt", "r+", encoding="UTF-8")
            content = file.read()
            print("Your To-Do List is:")
            print(content)
            file.close()
        else:
            break    

    else:
        print("Bye")    