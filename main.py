
def main():
     
    while True:
        
        answer = input("do you want to add a new To-Do item? y/n  or exit: ")

        if answer  == "y":
            task = input("type in his new To-Do item : ")
            file = open("to_do.txt", "a", encoding="UTF-8")
            file.write(task+'\n')
            file.close()
                
        elif answer == "n":
            list_todo=input("do you want to list your To-Do items ? y/n :  ")
            
            if list_todo == "y":
                file = open("to_do.txt","r",encoding="UTF-8")
                read_file = file.readlines()
                file.close()
                if read_file:
                    for index, line in enumerate(read_file,start=1):
                        print(f"{index}. {line.strip()}")
                print()

        elif answer == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break
            
        else: 
            print("tyr agian")

main()



     
