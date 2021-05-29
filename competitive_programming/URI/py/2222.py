a = int(input())

while a > 0:
    c = []
    b = int(input())
    
    for i in range(0, b):
        d = list(map(int,input().split()))
        c.append(d[1:])
    f = int(input())
    p = []
    for y in range(0, f):

        k = list(map(int,input().split()))
        p.append(k)
    for i in range(0, f):
        p1 = [] 
        p2 = [] 
        r = []
        p1 = list(c[p[i][1] - 1])
        p2 = list(c[p[i][2] - 1])
        if p[i][0] == 1:
            r = list(set(p1).intersection(set(p2)))
        if p[i][0] == 2:
        
            r = list(set(p1).union(set(p2)))


        print(len((r)))

    a -= 1
