a = list(map(int, input().split()))

if a[3] == 1:
    if a[4] == 1:
        print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")

elif a[3] == 0:
    if a[4] == 1:
        print("Jogador 1 ganha!")
    else:
        if a[0] == 0:
            if ((a[1] + a[2])&1):
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        else:
            if ((a[1] + a[2])&1):
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")



