a = {1001:1.5,1002:2.5,1003:3.5,1004:4.5,1005:5.5}

b = int(input())
cont = 0
while b:

    i,k = map(int,input().split())
    cont += k*a[i]
    b -= 1
print("%.2f" %cont)
