import math as _

a = int(input())
b = (((1 -  _.sqrt(5))/2)**a)
c = (((1 +  _.sqrt(5))/2)**a)
print("%.1f" %((c-b)/_.sqrt(5)))
