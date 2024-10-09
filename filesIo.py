import datetime


def add_task_to_file(task: str):
    """
    This function opens tasks file and add the task given by the user
    :param task:
    :return:
    """
    tasksFile = open("todoList.txt", "a", encoding="utf-8")

    tasksFile.write(task + "\n")
    tasksFile.close()
    return "Task added successfully"


def printTasks():
    tasksFile = open("todoList.txt", "r", encoding="utf-8")
    # jsonTask = tasksFile.readline()
    tasks = tasksFile.readlines()

    print(" --- Your To-Do List --- ")
    for i, line in enumerate(tasks, start=1):

        print(f"{i}. {line.strip()}")
    print()
while True:

    print("----- To Do List App -----")

    user_input = input("ADD A TASK\" to your list [Y/N] or type [exit] to quit application ? ")
    if user_input.lower() == "exit":
        print("Thank you for using To-Do program, Come Again Soon")
        break
    elif user_input.lower() == "y":

        user_task: str = input("Enter Your Task: ")
        #  save it to file at a new line
        print(add_task_to_file(user_task))

    elif user_input.lower() == "n":

        user_choice = input("Do you want to \"LIST YOUR TO-DO ITEMS\" [Y/N] or type [exit] to quit application ? ")
        if user_choice.lower() == "exit":
            print("Thank you for using To-Do program, Come Again Soon")
            break
        elif user_choice.lower() == "y":
            printTasks()
            # print to do list one task per line then return
    else:
        print("Wrong input, please try again with a valid choice")
        input(" << Press any button to continue >> ")




