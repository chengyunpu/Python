s=str(input())
n=len(s)
t=0
for i in range(n):
    t+=ord(s[i])-64
print(t)