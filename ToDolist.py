#LAB_FILES_IO
while True:
    user_in=input("do you want to add a new To-Do item? answer by (y) for yes and (n) for no ")
    if user_in=='y':
        new_to_do_list=input("user to type in his new To-Do item : ")
        file = open('to_do.txt', "a", encoding="utf-8")
        file.write(new_to_do_list+"\n")
        file.close()
    elif user_in=='n':
        user_in2=input("do you want to add a new To-Do item? answer by (y) for yes and (n) for no ")
        if user_in2=='y':
            file=open('to_do.txt')
            print(file.read())
            file.close()
    elif user_in == 'exit':
        print("thank you for using the To-Do program, come back again soon")
        break
