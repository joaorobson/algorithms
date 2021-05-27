a = int(input())
maior = 0.0
while a:
    b,c = map(float,input().split())
    b = int(b)
    if c > maior:
        maior = c
        mat = b
    a -= 1 
if maior >= 8:
    print(int(mat))
else:
    print("Minimum note not reached")

