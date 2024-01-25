while True:
    try:
        a,b=map(int,input().split())
        s=list(map(int,input().split()))
        r=0
        l=0
        n=0
        for i in range (b):
            if(s[i]>a):
                r+=1
        l=b-r
        if(r>l):
            n=a
            for i in range (b):
                if(s[i]>a):
                    n=max(n,s[i])
            print(r,n)
        elif(r<l):
            n=a
            for i in range (b):
                if(s[i]<a):
                    n=min(n,s[i])
            print(l,n)
    except EOFError:
        break