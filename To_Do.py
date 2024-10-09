stop = False

while not stop:
    print()
    add_item = input('Do you want to add a new To-Do item? (y for yes and n for no.): ')
    if add_item.lower() == 'y':
        write = input('Type your To-Do item: ')
        file = open("to_do.txt", "a+", encoding="utf-8")
        file.write(write + '\n')
        file.close()
    elif add_item.lower() == 'n':
        print()
        list_item = input('Do you want to list your To-Do items? (y for yes and n for no.): ')
        if list_item.lower() == 'y':
            file = open("to_do.txt", "r", encoding="utf-8")
            file.seek(0)
            content = file.read().splitlines()
            print()
            print('Your To-Do items:>>>')
            print()
            for line in content:
                print(line)
            file.close()
        elif list_item.lower() == 'n':
            print()
            toExit = input('If you want to exit type "exit": ')
            if toExit.lower() == 'exit':
                print('Thank you for using the To-Do program, come back again soon!')
                print()
                stop = True
        elif list_item.lower() == 'exit':
            print('Thank you for using the To-Do program, come back again soon!')
            print()
            stop = True
        else:
            print('Wrong input! Try again please.')
    elif add_item.lower() == 'exit':
            print('Thank you for using the To-Do program, come back again soon!')
            print()
            stop = True
    else:
        print('Wrong input! Try again please.')
         