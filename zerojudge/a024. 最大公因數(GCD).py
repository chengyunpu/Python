def k(a,b):
        while b:
                r=a%b
                a=b
                b=r
        return(a)
a,b=map(int,input().split())
print(k(a,b))