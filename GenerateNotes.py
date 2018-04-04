
import os
import sys


def ScanDir(path):
    # list all dirs
    dirs = [x for x in os.listdir(path) if os.path.isdir(x)]

    # ignore dir startwith '.'
    dirs = [x for x in dirs if not x.startswith('.')]

    # ignore src dir
    dirs.remove('src')

    return dirs

def GenerateNotes(path):
    

        


if __name__ == '__main__':
    print(GenerateDirs())