while True:
    try:
        s=list(input())
        n=len(s)
        a=list(input())
        an=len(a)
        for i in range (an):
            k=True
            for j in range (n):
                if(a[i]==s[j]):
                    k=False
                    print(j+1,end=' ')
                    s[j]='#'
                    break
            if(k):
                print('X',end=' ')
        print()
    except EOFError:
        break