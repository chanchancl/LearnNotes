
# 序列迭代器

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))
'''
Traceback (most recent call last):
  File "e:\Program File\桌面\LearnPython\iterator.py", line 10, in <module>
    print(next(it))
StopIteration
'''

# 自定义迭代器

class Reverse:
    'Iterator fo looping over a sequence backwards.'
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)


