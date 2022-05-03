for a in range(30, 101):

#a = int(input())
    l = []
    for i in range(3):
        l.append((a+i)%4)
    print(a, " ", end="")
    if 1 in l:
        print(l.index(1), "A")
    elif 3 in l:
        print(l.index(3), "B")
    elif 2 in l:
        print(l.index(2), "C")
    elif 0 in l:
        print(l.index(0), "D")
