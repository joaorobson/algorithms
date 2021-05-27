a = input()
de = 10
vet = []
um = "I"
cinco = "V"
dez = "X"

cont = 2
vet.append("I")
for i in range(0,3):
    if de == 100:
        um = "X"
        cinco = "L"
        dez = "C"
    elif de == 1000:
        um = "C"
        cinco = "D"
        dez = "M"
    for i in range(0,9):
        if str(cont)[0] == "4":
            string = um + cinco
        elif str(cont)[0] == "9":
            string = um + dez
        elif str(cont)[0] == "5":
            string = cinco
        elif str(cont)[0] == "1" and len(str(cont)) > 1 and str(cont)[1] == "0":
            string = dez
        elif str(cont)[0] > "5":
            string = cinco + (cont-5)*um
        else:
            string = cont*um
        vet.append(string)
        cont += 1
    de *= 10
    cont = 2

de = 10
resp = ""
siz = 0
b="{}"
resp = ""
resp = b + resp
div = int(a)
while(div > 0):
    rest = div%de
    div = int(div/de)
    if siz + rest - 1 >= siz:
        resp = b + resp.format(vet[siz + rest - 1])

    siz += 9

print(resp.format(""))
