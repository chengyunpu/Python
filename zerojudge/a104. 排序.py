while True:
    try:
        n=int(input())
        s=list(map(int,input().split()))
        for i in range (n):
            for j in range (n):
                if(s[i]<s[j]):
                    s[i],s[j]=s[j],s[i]
        for k in range (n):
            print(s[k],end=' ')
        print()
    except EOFError:
        break