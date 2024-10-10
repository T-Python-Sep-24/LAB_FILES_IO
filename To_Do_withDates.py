from datetime import date
import json
import os

stop = False
if not os.path.exists('to_do.json') or os.path.getsize('to_do.json') == 0:
    with open('to_do.json', 'w') as file:
        json.dump({}, file)
    file.close()
while not stop:
    print()
    add_item = input('Do you want to add a new To-Do item? (y for yes and n for no.): ')
    if add_item.lower() == 'y':
        write = input('Type your To-Do item: ')
        item = {
                "content": write,
                "date": "(" + date.today().isoformat() + ")",
                "done": False
        }
        with open("to_do.json", 'r') as file:
            data = json.load(file)

        data[len(data)+1] = item

        with open("to_do.json", 'w') as file:
            json.dump(data, file, indent=4)
 
        file.close()
    elif add_item.lower() == 'n':
        done_item = input('Have you done a task? (y for yes and n for no.): ')
        if done_item.lower() == 'y':
            with open('to_do.json', 'r') as file:
                items = json.load(file)
            print()
            print('Your To-Do items:>>>')
            for key, item in items.items():
                print(f'{key}. {item['content']} {item['date']} - {item['done']}')
            
            id = input('Choose a task to set to be done (by its number!): ')
            items[id]["done"] = 'DONE'

            with open("to_do.json", 'w') as file:
                json.dump(items, file, indent=4)
    
            print()
            print('Your To-Do items after:>>>')
            for key, item in items.items():
                print(f'{key}. {item['content']} {item['date']} - {item['done']}')
                
            file.close()
        elif done_item.lower() == 'n':
            print()
            list_item = input('Do you want to list your To-Do items? (y for yes and n for no.): ')
            if list_item.lower() == 'y':
                with open('to_do.json', 'r') as file:
                    items = json.load(file)
                
                print()
                print('Your To-Do items:>>>')
                for key, item in items.items():
                    print(f'{key}. {item['content']} {item['date']} - {item['done']}')
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
         