from itertools import combinations
import re

a = input()

a = re.findall('Q|A', a)

b = list(combinations(''.join(a), 3))
c = 0
for i in b:
    if i == ('Q', 'A', 'Q'):
        c += 1

print(c)
