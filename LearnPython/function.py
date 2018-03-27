
# 内嵌参数
def foo():
    def bar():
        print('bar() called')
    print('foo() called')
    bar()

foo()

# 函数指针
def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 999999999)
print(convert(int, myseq))
print(convert(float, myseq))

# 固定参数
def foo2(who):
    print('Hello', who)

try:
    foo2()
except TypeError as e:
    print(e)

foo2('World!')
try:
    foo2('Mr.', 'World!')
except TypeError as e:
    print(e)

# 默认参数
def taxMe(cost, rate=0.0825):
    return cost + (cost * rate)

taxMe(100)
taxMe(100, 0.05)

# 默认参数，与固定参数，关键字参数混合
def net_conn(host, port=80, stype='tcp'):
    pass

net_conn('kappa', 8000)
net_conn(port=8080, host='chino')

net_conn('phaze', 8000, 'udp')
net_conn('kappa')
net_conn('chino',stype='icmp')
net_conn(stype='udp', host='solo')
net_conn('deli', 8080)
net_conn(port=81, host='chino')

def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    'display regular args and non-keyword variable args'
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    for eachXtrArg in theRest:
        print('    another arg:', eachXtrArg)

print('--------tupleVarArgs---------')
tupleVarArgs('abc')
tupleVarArgs(23, 4.56)
tupleVarArgs('abc', 123, 'xyz', 456.789)

def dictVarArgs(arg1, arg2='defaultB', **theRest):
    'display 2 regular args and keyword variable args'
    print('formal arg1:', arg1)
    print('formal arg2:', arg2)
    for eachXtrArg in theRest:
        print('    Xtra arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg])))

print('--------dictVarArgs---------')
dictVarArgs(233)
dictVarArgs(1220, 740.0, c='grail')
dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')
dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))


# 两种变长参数混合
print('--------混合参数---------')
def new_foo(arg1, arg2, *aTuple, **aDict):
    print('arg1:', arg1)
    print('arg2:', arg2)

    for arg in aTuple:
        print('    non-keyword arg : ', arg)
    for arg in aDict:
        print('    key-word arg %s : %s' %(arg,aDict[arg]))


new_foo(2, 4, *(6,8), **{'foo': 10, 'bar': 12, 'func': foo})
new_foo(10, 20, 30, 40, foo=50, bar=60)
aTuple = (6,7,8)
aDict = {'z': 9}
new_foo(1, 2, 3, x=4, y=5, *aTuple, **aDict)
