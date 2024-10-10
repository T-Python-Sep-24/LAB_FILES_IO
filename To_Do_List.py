

def todo():
    while True:
                
        uesr_w = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no and 'exit' for close :) ")

        if uesr_w == 'y': 
            file = open('to_do.txt','a+',encoding="utf-8")
            write_uesr = input("write in his new To-Do item :) ")
            file.write(write_uesr +'\n')
            file.close()
        elif uesr_w == 'n':
            uesr_r = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no :) ")
            if uesr_r =='y':
                with open("to_do.txt", "r" , encoding="utf-8") as file:
                    items = file.read()
                    print(items)
            elif uesr_r =='n':
                print(" write 'exit' for close :) ")
        elif uesr_w == 'exit':
            print('thank you for using the To-Do program, come back again soon :)')
            break
            
todo()