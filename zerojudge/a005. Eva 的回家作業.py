n=int(input())
while (n!=0):
        n-=1
        a,b,c,d=map(int ,input().split())
        if(b/a==c/b):
                e=b/a*d
                print("%d %d %d %d %d" % (a,b,c,d,e))
        else :
                e=b-a+d
                print("%d %d %d %d %d" % (a,b,c,d,e))