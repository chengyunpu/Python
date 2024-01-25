s=str(input())
j=False
n=0

for i in range (len(s)-1,-1,-1):
    if(s[i]!='0'):
        n=i
        j=True
        break
if(j):
    for i in range (n,-1,-1):    
        print(s[i],end='')
else :
    print('0')
