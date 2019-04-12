import os
import platform

dictName = "commandsDict.txt"

class command:
    maxCharCommand = 20;
    isValidCommand = False;
    value = ""
    def __init__(self, name):
        self.name = name;

def makeCommandNameCompatible(name, maxNumberChars):
    print("[-] Make command name compatible.")
    return ("@" * (maxNumberChars - len(name))) + name    

def commandValidation(name):
    print("[-] Validating command")
    response = False
    path = os.getcwd()
    if (platform.system() == "Linux"):
        path += "/" + dictName
    elif (platform.system() == "Windows"):
        path += "\\" + dictName
    file = open(path,'r')
    for line in file.readlines():
        strLine = str(line).replace("@", "").replace("\n", "")
        name = str(name).replace("@", "").replace("\n", "")
        if (strLine == name):
            response = True;
            break
    file.close()
    return response



