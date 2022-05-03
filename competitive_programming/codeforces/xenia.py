def or_(a, b):
    return a|b
def xor(a, b):
    return (a&~b)|(~a&b)

def opor(l):
    res = []
    for i in range(0, len(l), 2):
       res.append(or_(l[i], l[i+1]))
    return res

def opxor(l):
    res = []
    for i in range(0, len(l), 2):
       res.append(xor(l[i], l[i+1]))
    return res

def res(l):
    while len(l) > 1:
        l = opor(l)
        if len(l) <= 1:
            break
        l = opxor(l)
    return l[0]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(0, a[1]):
    c = list(map(int, input().split()))
    b[c[0] - 1] = c[1]
    print(res(b))

