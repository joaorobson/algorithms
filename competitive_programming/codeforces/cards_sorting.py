from collections import deque
a = input()

b = list(map(int, input().split()))
b = deque(b)
c = 0
while len(b):
    if b[0] == min(b):
        b.popleft()
    else:
        h = b.popleft()
        b.append(h)
    c += 1
print(c)
