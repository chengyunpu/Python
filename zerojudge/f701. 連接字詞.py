while True:
    try:
        s=str(input())
        n=len(s)
        ss=str(input())
        for i in range (n):
            if(s[i]!=' '):
                print(s[i],end='')
            elif(s[i]==' '):
                print(" "+ss,end=' ')
    except EOFError:
        break