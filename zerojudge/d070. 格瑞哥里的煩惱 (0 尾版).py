n=1
while n!=0:
        n=int(input())
        if(n!=0):
                if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
                        print("a leap year")
                else:
                        print("a normal year")
        else:
                break