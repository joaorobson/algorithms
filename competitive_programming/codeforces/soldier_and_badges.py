a = int(input())

b = list(map(int, input().split()))

b.sort()
c = 0
for i in range(1,len(b)):
    while b[i] == b[i-1] or b[i] < b[i-1]:
        b[i] += 1
        c += 1

print(c)
