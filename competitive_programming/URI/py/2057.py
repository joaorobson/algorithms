a,b,c = map(int,input().split())

r = a + b + c

if r < 0:
    r = 24 + r
elif r > 24:
    r = r - 24
print(r)

