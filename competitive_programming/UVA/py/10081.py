m while True:
    try:
        k, n = map(int,input().split())
        l = [[],[]]
        temp = []
        
        for i in range(0,k+1):
            l[1].append(1)
        

        for i in range(2,n+1):
            l.append([])
            for j in range(0, k+1):
                l[i].append(l[i-1][j])
                if j < k:
                    l[i][j] += l[i-1][j+1]
                if j > 0:
                    l[i][j] += l[i-1][j-1]
        res = 0
        for i in range(0, k+1):
            res += l[n][i]
        p = (res*100)/(k+1)**n
        print("%.5lf" %p)
            
    except:
        break

