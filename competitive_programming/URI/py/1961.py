jump,plmb = input().split()

a = list(map(int,input().split()))

for i in range(0, int(plmb)-1):
    if abs(a[i] - a[i+1]) > int(jump):
        print("GAME OVER")
        break
else:
    print("YOU WIN")
