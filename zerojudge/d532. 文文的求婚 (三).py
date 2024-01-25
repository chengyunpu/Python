while True:
    try:
        n=0
        a,b=map(int,input().split())
        for i in range (a,b+1):
            if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
                n+=1
        print(n)
    except EOFError:
        break