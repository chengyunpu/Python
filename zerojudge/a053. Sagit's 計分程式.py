while True:
        try:
                n=int(input())
                if(n>=0 and n<=10):
                        print(n*6)
                if(n>=11 and n<=20):
                        print(60+(n-10)*2)
                if(n>=21 and n<=40):
                        print(80+(n-20))
                if(n>40):
                        print(100)
                
        except EOFError:
                break