while True:
    try:
        h1,m1=map(int,input().split())
        h2,m2=map(int,input().split())
        t=((24-(h1+24-h2))%24)*60+(((60-(m1+60-m2))%60)%60)
        print("%d %d"% ((t//60-( m1>m2))%24,t%60))
    except EOFError:
        break
