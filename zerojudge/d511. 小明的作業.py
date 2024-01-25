n=0
while True:
    try:
        a,b,c=map(int,input().split())
        if(a+b>c and b+c>a and a+c>b):
            n+=1
    except EOFError:
        print(n)
        break