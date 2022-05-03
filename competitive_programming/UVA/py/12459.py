
v = []
v.extend((1,2))
pri = 1
seg = 2
for i in range(0,78):
    ter = pri + seg
    pri = seg
    seg = ter
    v.append(ter)

a = int(input())

while(a > 0):
    print(v[a-1])
    a = int(input())
