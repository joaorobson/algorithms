while True:
    l = [31,29,31,30,31,30,31,31,30,31,30,25]
    try:
        a = list(map(int,input().split()))

        if a[0] == 12:
            if a[1] == 24:
                print("E vespera de natal!")
            elif a[1] == 25:
                print("E natal!")
            elif a[1] > 25:
                print("Ja passou!")
            else:
                print("Faltam {} dias para o natal!".format(25-a[1])) 
        else:
            print("Faltam {} dias para o natal!".format(sum(l[a[0]-1::]) - a[1]))  
    except:
        break
