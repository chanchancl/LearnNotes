
def simpleGen():
    yield 1
    yield '2 --> punch!'

myG = simpleGen()
print(next(myG))
print(next(myG))

# print(next(myG))
'''
Traceback (most recent call last):
  File "e:\Program File\桌面\LearnPython\generator.py", line 10, in <module>
    myG.__next__()
StopIteration
'''

from random import randint

def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0, len(aList)-1))

for item in randGen(['rock', 'paper', 'scissors']):
    print(item)


# 翻转序列的  generator版

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('abcdef'):
    print(char)

