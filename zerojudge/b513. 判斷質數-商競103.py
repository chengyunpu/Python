while True:
    try:
        n=int(input())
        for j in range (n):
            a=int(input())
            k=True
            for i in range(2,a):
                if(a%i==0):
                    k=False
                    print("N")
                    break
            if(k):
                print("Y")
    except EOFError:
        break