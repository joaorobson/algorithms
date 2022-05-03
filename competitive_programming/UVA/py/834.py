
while(True):
    try:
        a = list(map(int,input().split()))
        num = a[0]
        den = a[1]
        aux = 0
        b = []
        b0 = 0
        i = 0
        while(den > 0):
            while(num>=den):
                num = num - den
                b0 += 1
            aux = num
            num = den
            den = aux
            b.append(b0)
            b0 = 0
        print("[",end='')
        print(b[0],end='')
        print(";",end='')

        for i in range(1,len(b)-1):
            print(b[i],end='')
            print(",",end='')
        print(b[len(b)-1],end='')
        print("]")
    except:
        break
