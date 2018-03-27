f = open("hello.py", 'r')
buffer = f.read(200)
lines = buffer.split('\n')
for i in lines:
	print(i)
f.close()
print ('hello')