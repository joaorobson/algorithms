def fat(n):

    i = n
    k = 1
    for j in range(0,i):
        k *= n
        n -= 1

    k = str(k).replace("0","")
    return k[len(k)-1]



while True:
    try:
        a = int(input())
        print(str(a).rjust(5),"->",fat(a))
    except:
        break
