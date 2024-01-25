while True:
    try:
        r,c=map(int,input().split())
        n = [[0] * c for _ in range(r)]
        for i in range(r):
            k=list(map(int,input().split()))
            for j in range(c):
                n[i][j]=k[j]
        for i in range(c):
            for j in range(r):
                print("%d "%(n[j][i]),end='')
            print()
    except EOFError:
        break