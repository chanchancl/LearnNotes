
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        '__init__ 是类的构造函数，在创建类的过程中会被自动调用'
        print('call __init__')
        self.data = []
    
    def __del__(self):
        '__del__ 是类的析构函数，当类的引用计数归0后，会被调用'
        pass
    
    @staticmethod
    def foo():
        print('calling static method foo()')


print(MyClass.__doc__)

# __dict__ 包括了类的一些预定义属性，和自定义属性
print(dict(MyClass.__dict__))

# create a instance
x = MyClass()
print(type(x.data))
xf = x.f
print(x.f())
x.foo()

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fibo')
e = Dog('Buddy')
print(d.kind, ' ', e.kind)
print(d.name, ' ', e.name)


class Animal(object):
    'One type of animal.'
    def __init__(self):
        self.name = ''

    def call(self):
        print('my name is %s' % self.name)
    
class Cat(Animal):
    def __init__(self):
        self.name = 'Cat'

class Dog(Animal):
    def __init__(self):
        self.name = 'Dog'


cat = Cat()
dog = Dog()

cat.call()
dog.call()

print(cat.__class__)
print(Cat.__base__)
print(Cat.__doc__)
print(dog.__class__)
print(Dog.__base__)


# 继承中的属性查找

print('查找属性')

class P1(object):
    def foo(self):
        print('called P1-foo()')

class P2(object):
    def foo(self):
        print('called P2-foo()')
    
    def bar(self):
        print('called P2-bar()')

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print('called C2-bar()')

class GC(C1, C2):
    pass

gc = GC()
print('call gc.foo()')
gc.foo()
print('call gc.bar()')
gc.bar()

print('call C2.bar(gc)')
C2.bar(gc)
print('call P2.bar(gc)')
P2.bar(gc)

print(GC.__mro__)

print('issubclass(GC,P1) : %s' % issubclass(GC,P1))
print('issubclass(C2,P1) : %s' % issubclass(C2,P1))
print('isinstance(gc,GC) : %s' % isinstance(gc,GC))
print('isinstance(gc,C1) : %s' % isinstance(gc,C1))