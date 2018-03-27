import sys

def this_failes():
	x = 1/0

try:
	this_failes()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)