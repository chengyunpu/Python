a,b=map(str,input().split())
k=True
for i in range (int(a),int(b)+1,1):
    s=str(i)
    t=0
    for j in range(len(s)):
        t+=int(s[j])**len(s)
    if (t==i):
        k=False
        print(i,end=' ')
if(k):
    print("none",end=' ')