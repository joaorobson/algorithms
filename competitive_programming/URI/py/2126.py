i = 1
while True:
    try:
        a = input()
        b = input()

        if not a in b:
            print("Caso #%d:" %i)
            print("Nao existe subsequencia")
            print()
        else:
            print("Caso #%d:" %i)
            print("Qtd.Subsequencias: %d" %b.count(a))
            print("Pos: %d" %(b.rfind(a) + 1))
            print()
        i += 1
    except:
        break
