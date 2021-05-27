a = int(input())
while a != 0:
    soma = 0
    b = []
    for i in range(0, a):
        c = 100*float(input())
        b.append(c)
    d = round(sum(b)/a)

    for i in b:
        if i < d:
            soma += d-i
    print('$%.2f' %(soma/100))
    a = int(input())
