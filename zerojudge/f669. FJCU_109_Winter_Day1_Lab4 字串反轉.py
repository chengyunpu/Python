while True:
    try:
        s=str(input())
        n=len(s)
        for i in range (n-1,-1,-1):
            print(s[i],end='')
    except EOFError:
        break
