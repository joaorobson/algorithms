p = True
while True:
    try:
        a = list(map(int,input()))
        d = False
        b = False 
        c = 0
        if not p:
            print()
        if p:
            p = False
        if ((a[len(a)-2]*10 + a[len(a)-1])%4==0 and (a[len(a)-2] != 0 or a[len(a)-1] != 0)) or (a[len(a)-4]*1000 + a[len(a)-3]*100+ a[len(a)-2]*10 + a[len(a)-1])%16==0:
            
            print("This is leap year.")
            b = True
            d = True
        if sum(a)%3==0 and (a[len(a) - 1] == 0 or a[len(a)-1] == 5):
            print("This is huluculu festival year.")
            d = True

        if (a[len(a) - 1] == 0 or a[len(a)-1] == 5):
            for i in range(0, len(a)):
                if i&1:
                    c += -1*a[i] 
                else:
                    c += a[i]
            if c%11 == 0 and b:
                print("This is bulukulu festival year.")

                d = True
        if not d:
            print("This is an ordinary year.")
    except:
        break
