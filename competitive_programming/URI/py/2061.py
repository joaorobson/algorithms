a = list(map(int, input().split()))
n = a[0]

for i in range(0, a[1]):
    b = input()
    if b == "fechou":
        n += 1

    elif b == "clicou":
        n -= 1

print(n)
