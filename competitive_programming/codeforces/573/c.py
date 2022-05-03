n, m, k= list(map(int, input().split()))

p = list(map(int, input().split()))

ops = 0

b = p[0]

if not b%k:
    l = b
elif b > k:
    l = (b//k)*k + k
else:
    l = k
print('l', l)
while(len(p)):
    b = list(p)[0]
    print(b, p, l)
    while(b <= l):
        p = p[1:]
        if len(p):
            b = list(p)[0]
        else:
            break
    l += k
    ops += 1
print(ops)  
