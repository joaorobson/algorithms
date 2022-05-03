a = int(input())

def fat(n):
    i = n
    res = 1
    while i:
        
        res = res*i
        i -= 1
    return res
while a > 0:
    if a == 1:
        print(0)
    elif a == 2:
        print(1)
    else:
        print(int((a-1)*fat(a-1)/2))
    a = int(input())
