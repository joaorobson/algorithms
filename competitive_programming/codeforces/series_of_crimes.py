a = list(map(int, input().split()))
for i in range(0, a[0]):
    p = input()
    if p.find('*') >= 0:
        if list(p).count('*') == 2:
            pos1 = p.index('*') + 1
            pos2 = p.rindex('*') + 1
        elif list(p).count('*') == 1:
            missl = i+1
            missc = p.index('*') + 1

if missc == pos1:
    res = pos2
else:
    res = pos1
print(missl, res)
