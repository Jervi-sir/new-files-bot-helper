#this is an All in One file

#----- [ Helpers ] -----
#save file of files name in file
import pickle
from pathlib import Path

def saveNames(filename, arrayName):
        with open(filename, 'wb') as outp:
                pickle.dump(arrayName, outp, pickle.HIGHEST_PROTOCOL)
                return True
#open fileNames
def openFile(filename):
    if not(os.path.exists(filename)):
        with open(filename, 'wb') as outp:
            pickle.dump([], outp, pickle.HIGHEST_PROTOCOL)
    with open(filename, 'rb') as f:
        data = pickle.load(f)
        return data

def getCurrentPath():
    return Path.cwd()

#----- [ runnable code ] -----

import os
print("\033[0;37;40m bot startssssssssss bruh \033[0m ")

filename = 'filesVisited.pkl'
currentPath = getCurrentPath()

#open database (kinda) if exisiting, or creating it if doesnt
fileToTest = openFile(filename)

print("\033[0;33;44m saved file opened \033[0m ")
#read file names existing in the folder
for file in os.listdir(currentPath):
    if file.endswith(".mp4"):       #if its an mp4
        if file in fileToTest:      #remove if already saved
            os.remove(file)
            print("\033[1;33;40m file exists,\t\t so removed \033[0m ")
        else:
            print("\033[1;32;40m file doesnt exist,\t so saved \033[0m ")
            fileToTest.append(file) #save if its new
    
#resave names in the file
print("\033[0;33;42m result saved \033[0m ")
saveNames(filename, fileToTest)

