import math
i = int(input())
l = 1
while i:
    def maior(n):
        if n == 0:
            return -1
        k = math.floor(math.log10(n) + 1) 
        a = ''
        if k < 4:
            a = (4-k)*'0' 
        n = a + str(n)

        if len(set(n)) == 1:
            return -1
        n = list(map(int, list(''.join(n))))
        n.sort()
        return int(''.join(str(i) for i in n[::-1]))

    def menor(n):
        if n == 0:
            return -1
        k = math.floor(math.log10(n) + 1) 
        a = ''
        if k < 4:
            a = (4-k)*'0' 
        n = a + str(n)
        if len(set(n)) == 1:
            return -1
        n = list(map(int, list(''.join(n))))
        n.sort()
        return int(''.join(str(i) for i in n))




    def kaprekar(n):
        c = 0
        while n != 6174:
            ma = maior(n)
            me = menor(n)
            if ma == -1 or me == -1:
                return -1
            n = ma - me
            c += 1
        return c
    a = int(input())
    b = str(a)
    print("Caso #{}: ".format(l) + str(kaprekar(a)))
    l+=1
    i -= 1
