m = [ [ None for i in range(2) ] for j in range(40) ]

def fib(n,c=0):
    if m[n][0]:
        return m[n][0], m[n][1]
    elif n == 0:
        m[n][0] = 0
        m[n][1] = 1
        return 0, c + 1
    elif n == 1:
        m[n][0] = 1
        m[n][1] = 1
        return 1, c + 1
    a, b, d, e = fib(n-1, c) + fib(n-2, c)
    m[n][0] = a + d
    m[n][1] = b + e + 1
    return a + d, b + e + 1


a = int(input())

while a:
    b = int(input())
    r = fib(b)
    print('fib({}) = {} calls = {}'.format(
            b, r[1] - 1,r[0]))

    a -= 1

