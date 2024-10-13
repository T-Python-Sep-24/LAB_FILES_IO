import tasksModule
import readWriteModule

tasksDict: dict = readWriteModule.readJson()

while True:
    print("Pick: \n" +
          "1: to add a task\n"+
          "2: to list your tasks\n" +
          "3: to mark down a task as done\n" +
          "4: to search a task using a title\n" +
          "5: to exit")
    pick: int = input("Enter: ")

    if pick == "1":
        tasksModule.addTask(tasksDict)
        
    elif pick == "2":
        tasksModule.listTasks(tasksDict)

    elif pick == "3":
        tasksModule.markTask(tasksDict)

    elif pick == "4":
        tasksModule.searchTasks(tasksDict)

    elif pick == "5":
        readWriteModule.writeJson(tasksDict)
        print("Thank you for using the To-Do program, come back again soon")
        break
    else:
        print("==== Wrong input ====")
        input("")

