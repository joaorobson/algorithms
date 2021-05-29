a = list(map(int, input().strip().split()))
m = []
t = []
for i in range(0, a[0]):
    h = input()
    s = list(map(int,h.strip().split()))
    m.append(s)
    s = []
o = False
for i in range(1, a[0] - 1):
    for k in range(1, a[1] - 1):
        if m[i][k] == 42:
            if m[i-1][k-1] == 7 and  m[i-1][k] ==7 and m[i-1][k+1] == 7:
                if m[i][k-1] == 7 and m[i][k+1] == 7 and  m[i+1][k-1] == 7:
                    if m[i+1][k] ==7 and  m[i+1][k+1] == 7:
                        print(i+1, k+1)
                        o = True
                        break
    if o:
        break
else:
    print(0,0)

