while True:
    try:
        a, b = input().split()

        c = input()
        d = input()

        cd = {}
        dd = {}
        for ix, i in enumerate(c.lower()):
            cd[i] = d[ix].lower()
            dd[d[ix].lower()] = c[ix].lower()
        for i in range(int(b)):
            ans = ""
            e = input()
            for k in e:
                if cd.get(k.lower()):
                    ans += cd.get(k.lower()) if k.islower() or (ord(k) > 122 or ord(k) < 65) else cd.get(k.lower()).upper()
                elif dd.get(k.lower()):
                    ans += dd.get(k.lower()) if k.islower() or (ord(k) > 122 or ord(k) < 65) else dd.get(k.lower()).upper()
                else:
                    ans += k if k.islower() else k.upper()
            print(ans)
        print('')
    except EOFError:
        break
