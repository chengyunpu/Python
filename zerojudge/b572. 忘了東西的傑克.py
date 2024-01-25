n=int(input())
for i in range (n):
    H1,M1,H2,M2,t=map(int ,input().split())
    if(((H2-H1)*60+M2-M1)>=t):
        print("Yes")
    else :
        print("No")