import math as m
def primes(k):
  :  if k == 1 or k == 2:
        return True
    if k&1 != 1:
        return False
    for j in range(3,int(m.sqrt(k)+1),2):
        if k%j == 0:
            return False
    else:
        return True


a = int(input())

while a:
    b = int(input())
    if primes(b):
        print('Prime')
    else:
        print('Not Prime')

    a -=1
