s=str(input())
n=len(s)
for i in range(n-1):
    print(ord(s[i]),end='_')
print(ord(s[n-1]),end='')