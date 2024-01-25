while True:
    try:
        a,b=map(int,input().split())
        t=0
        for i in range (a,b+1,1):
            k=True
            for j in range (2,i,1):
                if(i%j==0):
                    k=False
                    break
            if(k):
                t+=1
        print(t)
    except EOFError:
        break