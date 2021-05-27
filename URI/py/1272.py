a = int(input())
for i in range(0,a):
    b = input().split(' ')
    b = ''.join([''.join([i for i in p[0]]) for p in b if p])
    print(b)

