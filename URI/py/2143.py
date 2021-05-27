a = int(input())
while a != 0:
    while a:
        b = int(input())
        if b&1:
            print((b-1)*2+1)

        else:
            print((b-2)*2+2)
        a -= 1
    a = int(input())
