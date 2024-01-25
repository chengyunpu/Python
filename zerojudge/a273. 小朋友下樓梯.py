while True:
    try:
        n,k=map(int,input().split())
        if(n==0):
            print("Ok!")
        elif(k==0):
            print("Impossib1e!")
        elif(n%k==0):
            print("Ok!")
        else :
            print("Impossib1e!")
    except EOFError:
        break