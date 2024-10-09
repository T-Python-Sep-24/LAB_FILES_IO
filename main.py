# filee = open("to_do.txt" , "x", encoding="UTF-8")
# filee.close()

check = input("do you want to add a new To-Do item?")

filee = open("to_do.txt","a", encoding="UTF-8")

while check == "y":
    keepValue = input("what is type in his new To-Do item?")
    filee.write(keepValue + "\n")

    check = input("do you want to add a new To-Do item?")
    if check == "exit": 
        filee.close()
        break

filee = open("to_do.txt","r", encoding="UTF-8") 
content = filee.read()
print(content)   
filee.close()    

print("thank you for using the To-Do program, come back again soon")