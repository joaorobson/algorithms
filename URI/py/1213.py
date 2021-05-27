import math

def ones():
    l = []
    for i in range(1,1000):
        l.append(int(i*'1'))
    return l

a = int(input())
if a == 1:
    print(1)
else:
    h = ones()
    for j in range (1,10000):
        n = math.floor(math.log10(j)+1)
        c = n
        for i in h[n:]:
            c += 1
            if i%j == 0 and j == :
                print(j,i)
                break
