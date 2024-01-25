def k(n):
    if(n==1):
        print("1")
        return
    for i in range(2,n+1):
        p=0
        while(n%i==0):
            p+=1
            n/=i
        if(p!=0):
            if(p==1):
                print("%d " % (i),end='')
            else :
                print("%d^%d " %(i,p),end='')
            if(n>1):
                print("* ",end='')
                
while True:
    try:
        n=int(input())
        k(n)
    except EOFError:
        break