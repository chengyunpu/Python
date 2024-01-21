k=int(input())
i=1
while(i!=k+1):
        n=int(input())
        if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
                print("Case "+str(i)+": a leap year")
        else:
                print("Case "+str(i)+": a normal year")
        i+=1