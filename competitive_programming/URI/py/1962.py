a = int(input())

for i in range(0,a):
    b = int(input())

    if(2015 - b <= 0):
        print(b-2014,"A.C.")
    else:
        print(2015-b,"D.C.")
