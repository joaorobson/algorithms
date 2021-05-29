def pascal_triangle():
    a = []
    a.append([1])
    a.append([1,1])
    for i in range(2,41):
        p = []
        for k in range(0, i+1):
            if k == 0 or k == i:
                p.append(1)
            else:
                p.append(a[i-1][k-1] + a[i-1][k])
        a.append(p)
    return a

def paths():
    t = pascal_triangle()
    k = 1
    p = []
    s = 0
    for i in range(1, 41):
        k = i
        for j in range(0, i):
            if k < j:
                break
            s += t[k][j]
            k -= 1
        p.append(s)
        s = 0
    return p



a = int(input())
p = paths()
while a:
    print(p[a-1])
    a = int(input())


