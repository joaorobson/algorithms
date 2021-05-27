while True:
    try:
        a = float(input())
        b = float(input())
        r = (3.14*((b/2.0)**2))
        h = a/r
        print("ALTURA = %.2f\nAREA = %.2f" %(h,r))
    except:
        break
