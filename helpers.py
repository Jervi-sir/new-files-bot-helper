#save file of files name in file
import pickle
from pathlib import Path

def saveNames(filename, arrayName):
        with open(filename, 'wb') as outp:
                pickle.dump(arrayName, outp, pickle.HIGHEST_PROTOCOL)
                return True
#open fileNames
def openFile(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
        return data

def getCurrentPath():
    return Path.cwd()