while True:
        try:
                n=int(input())
                for i in range(1,n+1):
                        for j in range(n-i):
                                print('_',end='')
                        for k in range (1,i*2):
                                print("*",end='')
                        for t in range (n-i):
                                print('_',end='')
                        print()
        except EOFError:
                break