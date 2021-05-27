def func(x):
    return x[1]

a = int(input())

lu = []
ll = []

for i in range(a):
    b = input()
    ll.append((b, b.lower(), (1 if b.islower() else 0)))

ll = (sorted(ll, key= lambda x:x[2]))
ll = sorted(ll, key = func)

for i in ll:
    print(i[0])
