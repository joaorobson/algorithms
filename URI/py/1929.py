a = list(map(int,input().split()))
a.sort()

if(a[1]+a[2]>a[3] or a[0]+a[1]>a[2]):
    print("S")
else:
    print("N")
