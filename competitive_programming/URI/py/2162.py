a = int(input())
b = list(map(int, input().split()))
def foo(b):
    s = []
    for i in range(0, len(b)-1):
        if b[i] < b[i+1]:
            s.append('p')
        elif b[i] > b[i+1]:
            s.append('v')
        else:
            break
        if len(s) >= 2 and s[i - 1] == s[i]:
            break
    else:
        print(1)
        return
    print(0)

foo(b)
