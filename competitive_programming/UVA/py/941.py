from math import factorial as f
a = int(input())

while a:
    b = input()
    c = int(input())
    mini = 0
    h = b
    fac = f(len(b)-1) 
    p = 1
    maxi = f(len(b)-p)-1 
    ans = ''
    cont = 0
    for i in range(0, len(b)- 1):
        while c > maxi:
            mini = maxi + 1
            maxi += fac 
            cont += 1
        p += 1
        fac = f(len(b)-p) 
        maxi = mini + fac - 1
        ans += h[cont]
        h = h.replace(h[cont],'')
        h = ''.join(sorted(h))
        cont = 0
    ans += h[0]
    print(ans)
    a -= 1
print()
