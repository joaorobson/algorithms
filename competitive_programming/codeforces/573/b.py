a = input().split()

d = {}
ds = {}
for i in a:
    if d.get(i[1]):
        d[i[1]].append(int(i[0]))
        d[i[1]].sort()
        ds[i[1]] += 1
    else:
        d[i[1]] = [int(i[0])]
        ds[i[1]] = 1

ds = dict(sorted(ds.items(), key = lambda x:x[1], reverse=True))
for i in ds:
    if ds[i] == 3:
        if len(set(d[i])) == 1:
            print(0)
            break
        elif len(set(d[i])) == 2:
            print(1)
            break
        elif d[i][2] == (d[i][1] + 1) and d[i][1] == (d[i][0] + 1):
            print(0)
            break
        elif d[i][1] == (d[i][0] + 1) or d[i][1] == (d[i][0] + 2):
            print(1)
            break
        elif d[i][2] == (d[i][1] + 1) or d[i][2] == (d[i][1] + 2):
            print(1)
            break
        else:
            print(2)
            break

    elif ds[i] == 2:
        if len(set(d[i])) == 1:
            print(1)
            break
        elif d[i][1] == (d[i][0] + 1) or d[i][1] == (d[i][0] + 2):
            print(1)
            break
    else:
        print(2)
        break


