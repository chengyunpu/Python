import math
while True:
        try:
                a=b=c=0
                n=int(input())
                for i in range (n):
                        c=0
                        a=int(input())
                        b=int(input())
                        for j in range(a,b+1):
                                if(math.sqrt(j)==int(math.sqrt(j))):
                                        c+=j
                        print("Case %d: %d"%(i+1,c))
        except EOFError:
                break