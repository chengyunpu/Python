while True:
    try:
        a=int(input())
        s=list(map(int,input().split()))
        n=len(s)
        t=0
        for i in range (n):
            if(s[i]==0):
                r=s[i+1] if i+1<n else s[n-2]
                l=s[i-1] if i-1>=0 else s[1]
                t+=min(r,l)
        print(t)
    except EOFError:
        break