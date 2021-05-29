from decimal import Decimal

a = input()
if a[0] != "-":
    print("+",end="")
print('%.4E' % Decimal(a))
