def f(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

a, b = list(map(int, input().split()))

lin = []
m = []
l = 0
co = 0
ans = 0
for i in range(a):
    c = input()
    c = c.replace(" ", "")
    for ix ,ca in enumerate(c):
        lin.append(ca)
        if ca == '1':
            l = i
            co = ix
        elif ca == '.':
            ans += 1
    m.append(lin)
    lin = []
print(ans, (co+1)*l)
res = f(ans - (co+1)*l)%(10**9+7)
print(m, res)
