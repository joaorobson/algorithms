import sys

a = int(input())
b_a = list(map(int,sys.stdin.readline().split()))
b = []
c = []
for t in b_a:
    b.append(int(t))
soma = sum(b)
i = 0
c.append(0)
while True:
    if i < 0 or i >= len(b) or b[i] == 0:
        break
    else:
        num = b[i]
        b[i] -= 1
        if i not in c:
            c.append(i)
        if num&1:
            i += 1
        else:
            i -= 1

print(len(c),sum(b))


