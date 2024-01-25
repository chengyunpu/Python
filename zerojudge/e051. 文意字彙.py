s=str(input())
n=len(s)
print(s[0],end='')
for i in range(1,n-1):
    print('_',end='')
print(s[n-1],end='')