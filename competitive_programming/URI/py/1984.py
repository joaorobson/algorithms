a = list(input().strip())
b = len(a)
c = b
for i in range(0,int(b/2)):
    f = a[i]
    a[i] = a[c-i-1]
    a[c-i-1] = f
h = "".join(a[:c:])
print("%s" %h)
