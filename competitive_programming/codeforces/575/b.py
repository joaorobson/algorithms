global tree
tree = [0]*15
def st(tree,l, n, s, e):
    if s == e:
        tree[n] = l[s]
        return tree[n]
    else:
        m = (s+e)//2
        tree[n] = st(tree, l, 2*n+1, s, m) + st(tree, l, 2*n+2, m+1, e)
    return tree[n]

def sumt(n, qs, qe, s, e):
    if qs <= s and qe >= e:
        return tree[n]
    if qs > e or qe < s:
        return 0

    m = s + (e-s)//2
    p1 = sumt(n*2+1, qs, qe, s, m)
    p2 = sumt(n*2+2, qs, qe, m+1, e)
    return p1+p2

l = [1,3,5,7,9,11]

(st(tree, l, 0, 0, len(l)-1))
print(tree)
print(sumt(0, 1, 3, 0, 5))
