a = list(map(int,input().split()))

if a[0] == a[1]:
    print(a[0])
elif a[0] != a[1]:
    print(a[0]) if a[0] > a[1] else print(a[1])
