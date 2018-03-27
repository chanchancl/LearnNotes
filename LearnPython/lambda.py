
def true1():
    return True

def true2(): return True

true3 = lambda : True

func = [true1, true2, true3]

for fun in func:
    print(type(fun))
    print(fun)
    print(fun())


# apply, filter, map, reduce

# apply 已经没必要使用了

# filter

# version 1
from random import randint

def odd(n):
    return n % 2

allNums = []
for eachNum in range(20):
    allNums.append(randint(1, 99))
print(list(filter(odd, allNums)))

# version 2

print(list(filter(lambda n: n%2, allNums)))

# version 3

print([ n for n in allNums if n%2])


# map

print(list(map(lambda x: x+2, [0, 1, 2, 3, 4, 5])))
print([x+2 for x in range(6)])
print([x**2 for x in range(6)])
print(list(map(lambda x, y: x + y, [1,3,5], [2,4,6])))


# reduce 这个貌似删掉了
'''

def mySum(x, y): return x + y

allNums = range(5)
total = 0

# version 1
for eachNum in allNums:
    total = mySum(total, eachNum)
print('the total is: %d' % total)

# version 2
total = 0
print('the total is: %d', reduce(lambda x,y: x+y, range(5)))

'''