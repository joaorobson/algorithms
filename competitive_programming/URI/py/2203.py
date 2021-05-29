import math

while True:
    try:
        a = list(map(int, input().split()))
        d1 = math.sqrt((a[0] - a[2])**2 + (a[1]-a[3])**2) + a[4]*1.5
        if d1 <= a[5] + a[6]:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
