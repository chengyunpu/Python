while True:
    try:
        n=int(input())
        k=[0]*30
        i=0
        while(n>0):
            k[i]= n%2
            n//=2
            i+=1
        for j in range(i-1,-1,-1):
            print(k[j],end='')
        print()
    except EOFError:
        break