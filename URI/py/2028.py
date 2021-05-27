def fat(n):
    i = n
    soma = 1
    r = []
    r.append(0)
    for j in range(1,i+1):
        k = j
        while k > 0:
            r.append(j)
            k -= 1
    return r
i = 1
while True:
    try:
        a = int(input())
        if a == 0:
            print("Caso %d: %d numero" %(i,len(fat(a))))
        else:
            print("Caso %d: %d numeros" %(i,len(fat(a))))
        print(*fat(a))
        print()
        i += 1
    except:
        break
