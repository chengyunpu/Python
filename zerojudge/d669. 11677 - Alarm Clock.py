while True:
    try:
        h1,m1,h2,m2=map(int,input().split())
        if(h1==h2==m1==m2==0):
            break
        print(((h2 - h1) * 60 + m2 - m1 + 24 * 60) % (24 * 60))
    except EOFError:
        break