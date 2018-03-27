
listA = [1,3,5]
listB = [2,4,6]

listA.append(7)
print(listA)

listA.remove(7)
listA.extend(listB)
print(listA)
listA.sort()
print("After sort ", listA)

listC = list("abcdefg")
print("'abcdefg' index of d : ", listC.index('d'))

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("count of apple : ", fruits.count('apple'))


''' 1
squares = []
for x in range(10):
	squares.append(x**2)
'''
# 2
# squares = list(map(lambda x: x**2, range(10)))
# 3
squares = [x**2 for x in range(10)]
print(squares)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

print([(x, x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]
print( [ [row[i] for row in matrix] for i in range(4)])

for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))



