while True:
        try:
                n=int(input())
                
                for i in range(n):
                        a=1
                        k=str(input())
                        for j in range(len(k)):
                                a*=int(k[j])
                        print(a,"\n")
                        
        except EOFError:
                break