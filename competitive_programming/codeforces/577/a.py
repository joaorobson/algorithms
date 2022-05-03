n, m = list(map(int, input().split()))
r = m*[n*[None]]
print(r)
co = 0
for i in range(n):
    b = input()
    co = 0
    for j in (b):
        print(co, i, j)
        r[co][i] = j
        print('iiii',r)
        co += 1
c = input()
print(r)
