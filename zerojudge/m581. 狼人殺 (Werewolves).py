while True:
    try:
        n=int (input())
        s=list(map(int,input().split()))
        t=w=0
        for i in range(n):
            if(s[i]==0 or s[i]==1):
                t+=1
            elif(s[i]==-1):
                w+=1
        v=False
        while(True):
            k=int(input())
            if k==0:
                break
            elif(k>0) :
                if(s[k-1]==3):
                    v=True
                    break
                if(s[k-1]==0 or s[k-1]==1):
                    t-=1
                    s[k-1]=3
                elif(s[k-1]==-1):
                    w-=1
                    s[k-1]=3
        if(v):
            print("Wrong")
            break 
        elif(w>0 ):
            print("Werewolves")
            break
        elif(w==0 ):
            print("Townsfolk")
            break
    except EOFError:
        break