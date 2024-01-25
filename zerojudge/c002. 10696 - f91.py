while True:
    try:
        n=int(input())
        if(n==0):
            break
        def f91(n):
            if(n<=100):
                return f91(f91(n+11))
            elif(n>=101):
                return n-10
        print("f91(%d) = %d"%(n,f91(n)))
    except EOFError:
        break
        
