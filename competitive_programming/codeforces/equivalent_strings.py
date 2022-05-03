a = input()

b = input()


def equivalent(a, b):
    if len(a) != len(b) or len(a)&1 == 1 or len(b)&1 == 1:
        return False
    if len(a) == 0 or len(b) == 0:
        return False
    if a == b or a[::-1] == b or a == b[::-1]:
        return True

    else:
        a1 = a[:int(len(a)/2)]
        a2 = a[int(len(a)/2):]
        b1 = b[:int(len(b)/2)]
        b2 = b[int(len(b)/2):]
        if len(a1) == 0 or len(b1) == 0 or len(a2) == 0 or len(b2) == 0:
            return False

        if equivalent(a1, b1) and equivalent(a2,b2):
            return(True)
        elif equivalent(a1, b2) and equivalent(a2, b1):
            return (True)
        else:
            return False

if (equivalent(a,b)):
    print('YES')
else:
    print('NO')
