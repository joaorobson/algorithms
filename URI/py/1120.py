a = input().split()

while (a[0], a[1]) != ('0','0'):
    b = a[1].replace(a[0],'')
    if b.count('0') == len(b) or len(b) == 0:
        print(0)
    else:
        print(int(b))
    a = input().split()


