while True:
    try:
        a1,a2=map(int,input().split())
        b1,b2=map(int,input().split())
        c1,c2=map(int,input().split())
        for i in range (9999999999):
            if((i-a2)%a1==0 and (i-b2)%b1==0 and (i-c2)%c1==0):
                print(i)
                break
    except EOFError:
        break