from collections import deque

import functools
@functools.lru_cache(maxsize = 1000000)

def m():
    while True:
        try:
            a = input().strip()
        except EOFError:
            break
        a = ' '.join(a).split()
        b = deque() 
        pos = ""
        cont = 0
        aux = []
        cauda = True
        for i in a:
            if i == '[':
                if cauda:
                    b.append(''.join(aux))
                    aux = []
                else:
                    b.appendleft(''.join(aux))
                    aux = []
                cauda = False

            elif i == ']':
                if not cauda:
                    b.appendleft(''.join(aux))
                    aux = []
                else:
                    b.append(''.join(aux))
                    aux = []
                cauda = True 

            else:
                aux.append(i)
        if cauda:
            b.append(''.join(aux))
        else:
            b.appendleft(''.join(aux))


            
        print(''.join(b))

            

if __name__ == '__main__':
    m()



