n=int(input())
k=True
for i in range (2,n):
    if(n%i==0):
        k=False
        break
if(k):
    print("yes")
elif(k==False):
    print("no")