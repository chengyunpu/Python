while True:
    try:
        n=int(input())
        a=0
        for i in range (1,n+1):
            a+=i*i
        print(a)
    except EOFError:
        break