while True:

    a = list(map(int,input().split()))
    l = [2,5,10,20,50,100]
    o = 1
    m = []
    for i in range(0,len(l)-1):
        c = l[i]
        for j in range(o,len(l)):
            m.append(c+l[j])
        o += 1
    if a[0] == a[1] == 0:
        break

    else:
        if (a[1] - a[0]) > 150 or (a[1] - a[0]) not in m:
            print("impossible")
        else:
            print("possible")

