import json

def readJson():
    ''' read from the json file then return as Dict or an empty dict if there is no data'''

    try:
        with open("to_do.json", "r") as file:
            content = json.load(file)
            # check if the content is not a dict return an empty dict
            if type(content) == dict:
                print("inside f")
                return content
            else:
                print("inside else")
                return {}
    except:
        print("inside except")
        return {}
    

def writeJson(tasksDict):
    try:
        with open("to_do.json", "w") as file:
            json.dump(tasksDict, file, indent = 4)
    except Exception as e:
        print(f"something went wrong... {e}")
