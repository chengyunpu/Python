while True:
    try:
        n=int(input())
        if(n==0):
            break
        for i in range (n):
            for j in range(n-i-1):
                print("_",end='')
            for k in range (i+1):
                print("+",end='')
            print()
    except EOFError:
        break