
import os
import sys


def GenerateDirs():
    # list all dirs
    dirs = [x for x in os.listdir('.') if os.path.isdir(x)]

    # ignore dir startwith '.'
    dirs = [x for x in dirs if not x.startswith('.')]

    # ignore src dir
    dirs.remove('src')

    return dirs

if __name__ == '__main__':
    print(GenerateDirs())