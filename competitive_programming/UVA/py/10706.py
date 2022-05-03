a = int(input())

while a:

    b = int(input())

    a0 =1
    an = 1
    soma = 1
    i = 1
    
    while soma < b:

        soma_ant = soma
        soma = ((a0+an)*i)/2
        i+=1
        an += 1

    dif = b - soma_ant

    print(int(dif))

    a -= 1
