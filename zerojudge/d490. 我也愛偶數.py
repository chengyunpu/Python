a,b=map(int,input().split())
n=0
for i  in range(a,b+1):
    if(i%2==0):
        n+=i
print(n)