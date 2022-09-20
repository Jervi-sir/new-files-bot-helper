#--------------------------------
# a bot that remove already existing file in a json file
# so just run it in a folder, it will save names on json file
# while checking if already exists, if so it will delete the file
#--------------------------------

import os
from helpers import saveNames, openFile, getCurrentPath
print("\033[0;37;40m bot startssssssssss bruh \033[0m ")
filename = 'filesVisited.txt'
currentPath = getCurrentPath()

fileToTest = openFile(filename)

print("\033[0;33;44m saved file opened \033[0m ")
#read file names existing in the folder
for file in os.listdir(currentPath):
    if file.endswith(".mp4"):       #if its an mp4
        if file in fileToTest:      #remove if already saved
            os.remove(file)
            print("\033[1;33;40m file exists,\t\t so remove \033[0m ")
        else:
            print("\033[1;32;40m file doesnt exist,\t so save \033[0m ")
            fileToTest.append(file) #save if its new
    
#resave names in the file
print("\033[0;33;42m result saved \033[0m ")
saveNames(filename, fileToTest)


