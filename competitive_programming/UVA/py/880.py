import math

while(True):
    try:
        a = int(input())
        d = 1 + 4*2*a
        n = int((-1 + int(math.sqrt(d)))/2)
        soma = n*(n+1)/2
        while(soma < a):
            n +=1
            soma = n*(n+1)/2

        dif = soma - a
        print("%d/%d" %(1 + dif ,n - dif))






    except:
        break
