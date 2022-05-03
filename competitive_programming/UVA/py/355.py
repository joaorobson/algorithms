while(True):
    s = "0123456789ABCDEF"
    expo = 0
    res = 0
    dez = 10
    div = 1
    base_from,base_to,num = input().split()
    print(s.index(max(num)))
    if(s.index(max(num)) > int(base_from)):
        print(num,"is an illegal base",base_from,"number")
    else:
        while(div > 0):
            div = int(int(num)/dez)
            resto = int(int(num)%dez)
            res += resto*(int(base_from)**expo)
            expo += 1
            num = div
        print(res)
