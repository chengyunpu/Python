while True:
    try:
        s=0
        n=int(input())
        for i in range (1,n):
            if(n%i==0):
                s+=i
        if(s>n):
            print("盈數")
        elif(s<n):
            print("虧數")
        else:
            print("完全數")
    except EOFError:
        break