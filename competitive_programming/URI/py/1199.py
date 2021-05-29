a = input()
if(a[0] == "0" and a[1] == "x"):
    b = int(a,0)
else:
    b = int(a)



while(b>0):
    if(a[0] == "0" and a[1] == "x"):
        print(int(a,0))
    else:
        print("0x" + str(hex(int(a))).upper()[2:])
    a = input()
    if(a[0] == "0" and a[1] == "x"):
        b = int(a,0)
    else:
        b = int(a)
