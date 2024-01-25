while True:
    try:
        a,b,c=map(int,input().split())
        t=a+b+c
        m=max(a,b,c)
        def k(n):
            if(n==a):
                return 'A'
            elif(n==b):
                return 'B'
            else :
                return 'C'
        if(m>t-m):
            print(k(m))
        else :
            if(k(m)=='A'):
                print(k(max(b,c)))
            elif(k(m)=='B'):
                print(k(max(a,c)))
            else :
                print(k(max(a,b)))
    except EOFError:
        break