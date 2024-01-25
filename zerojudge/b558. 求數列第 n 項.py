while True:
    try:
        n=int(input())
        a=0
        for i in range (1,n+1):
            a+=i-1
        print(a+1)
    except EOFError:
        break