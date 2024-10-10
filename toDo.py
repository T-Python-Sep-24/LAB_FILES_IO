file = open("to_do.txt", "a", encoding="UTf-8")
def to_do(a):
    file.write(a + "\n")
while True:
   userop=input("do you want to add a new To-Do item?y/n ")
   if userop=="n":
       userNO=input("do you want to list your To-Do items ?y/n ")
       if userNO=="n":
           break
       elif userNO=="y":
           file=open("to_do.txt", "r", encoding="utf-8")
           content = file.read()
           print(content)
   elif userop=="y":
      user_yup =input("ask the user to type in his new To-Do item")
      to_do(user_yup)
   elif userop=="exit":
       break

file.close()



