n=int(input())
for i in range (n):
    s=list(map(int,input().split()))
    for j in range (3):
        for k in range(3):
            if(s[j]<s[k]):
                s[j],s[k]=s[k],s[j]
    if(s[2]**2==s[0]**2+s[1]**2):
        print("right triangle")
    elif(s[2]**2>s[0]**2+s[1]**2):
        print("obtuse triangle")
    else :
        print("acute triangle")