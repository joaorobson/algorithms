a = int(input())

# not working

while(True):
    b = int(input())

    b = -b if b < 0 else b

    inf = 0
    sup = b
    while(True):
        if(b == 0):
            mid = 3
            break
        else:
            mid = int((inf + sup)/2)
            n = mid*(mid+1)/2

            if(mid == sup - 1 or n == b):
                break
            elif(n > b):
                sup = mid
            elif(n < b):
                inf = mid

            sub = int(n - b)
            while(sub%2 != 0):
                mid += 1
                n = mid*(mid+1)/2
                sub = (n - b)

    print(mid)

    if(a > 1):
        print()
    a -= 1
