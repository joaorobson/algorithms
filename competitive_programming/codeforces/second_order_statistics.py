a = input()
b = list(map(int, input().split()))

b = list(set(b))
b.sort()
if len(b) <= 1:
    print('NO')
else:
    print(b[1])
