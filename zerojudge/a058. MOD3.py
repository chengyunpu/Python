while True:
        try:
                a=b=c=0
                n=int(input())
                for i in range (n):
                        temp=int(input())
                        if (temp%3==0):
                                a+=1
                        elif(temp%3==1):
                                b+=1
                        else :
                                c+=1
                print("%d %d %d"% (a,b,c))
        except EOFError:
                break