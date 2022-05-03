def fat(n):
    i = n
    s = 1
    while i > 0:
        s *= i
        i -= 1
    return s
    



a,b = map(int,input().split())
print(a*(((a)*(b+1))*((fat(b+1)/2*fat(b-1)))))

print(fat(5))

