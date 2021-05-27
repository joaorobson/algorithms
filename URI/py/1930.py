a = list(map(int,input().split()))
b = 0
for i in range(1,4):
    b = a[i] - 1 + b
b = a[0] + b
print(b)
