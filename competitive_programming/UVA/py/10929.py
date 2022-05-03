while True:

    a = input()

    if a == "0":
        break
    b = int(a[0])

    for i in range(1, len(a)):
        if i&1 or i == 0:
            b -= int(a[i])
        else:
            b += int(a[i]) 

    if b%11 == 0:
        print("{} is a multiple of 11.".format(a))
    else:
        print("{} is not a multiple of 11.".format(a))

