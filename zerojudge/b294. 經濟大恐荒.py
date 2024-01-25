while True:
    try:
        n=int(input())
        s=list(map(int,input().split()))
        temp=0
        for i in range (1,n+1):
            temp+=i*s[i-1]
        print(temp)
    except EOFError:
        break