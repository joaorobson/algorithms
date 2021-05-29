while True:
    try:
        a = input()

        b = a.split(":")
        h = int(b[0])*3600 + int(b[1])*60

        h = h + 60*60
        r = h - 8*3600
        if r < 0:
            r = 0
        print("Atraso maximo: %d" %(r/60))
    except:
        break
