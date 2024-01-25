while True:
    try:
        s=str(input())
        n=len(s)
        a=b=0
        for i in range(0,n,2):
            a+=ord(s[i])-48
        for i in range (1,n,2):
            b+=ord(s[i])-48
        print(abs(a-b))
    except EOFError:
        break