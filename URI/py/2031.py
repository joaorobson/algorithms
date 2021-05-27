a = int(input())

while a:
    b = input()
    c = input()
    d = {}
    d.update({b:1})
    d.update({c:2})
    if b == c:
        if b == "pedra":
            print("Sem ganhador")
        elif b == "papel":
            print("Ambos venceram")
        elif b == "ataque":
            print("Aniquilacao mutua")
    else:
        if "ataque" in d:
            print("Jogador %d venceu" %(d["ataque"]))
        else:
            print("Jogador %d venceu" %(d["pedra"]))
    a -= 1
