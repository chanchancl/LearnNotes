

a = 'DGJ-100/30'
b = 'DGJ－100'


# 标准 type
# 待检测 type
def isType(a,b):
    error = '－_＿'
    right = True
    for char in b:
        if char not in error:
            if char not in a:
                right = False

