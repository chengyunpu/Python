while True:
        try:
                n=list(map(int,input().split()))
                k=0
                for i in range (1,n[0]+1):
                        k+=float(n[i])
                if(k/n[0]>59):
                        print("no")
                else :
                        print("yes")
                print("\n")
        except EOFError:
                break