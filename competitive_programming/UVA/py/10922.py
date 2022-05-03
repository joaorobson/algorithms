
def n(u):
    if sum(u) != 9:
        if sum(u) == u[0]:
            global cont
            cont = 0
            return False
        else:
            u = list(map(int,str(sum(u))))
            cont += 1
            return n(u)
    else:
        return True 
while True:


    cont = 1
    a = input()
    if a == "0":
        break
    t = len(a)
    c = []
    for i in range(0,t):
        c.append(int(a[i]))
    
    if n(c) == True:
        print("{} is a multiple of 9 and has 9-degree {}.".format(a, cont))
    else:
        print("{} is not a multiple of 9.".format(a))

    
