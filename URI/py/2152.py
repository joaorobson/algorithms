a = int(input())
while a:
    b = input().split()
    print('{}:{} - A porta {}!'.format(b[0].rjust(2,'0'),
            b[1].rjust(2,'0'), 'abriu' if int(b[2]) else 'fechou'))
    a -= 1

