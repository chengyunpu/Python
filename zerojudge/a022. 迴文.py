s=str(input())
t=len(s)
for i in range (len(s)):
        if(s[i]!=s[t-1]):
                print("no")
                break
        else :
                print("yes")
                break