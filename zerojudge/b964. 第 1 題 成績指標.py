while True:
    try:
        n = int(input())
        s = list(map(int, input().split()))

        w = True
        b = True

        for i in range(n):
            if s[i] >= 60:
                w = False
                break

        for i in range(n):
            if s[i] < 60:
                b = False
                break

        for i in range(n):
            for j in range(n):
                if s[i] < s[j]:
                    s[i], s[j] = s[j], s[i]
                    
        for i in range (n):
            print(s[i],end=' ')
        print()
        if w:
            print(max(s))
            print("worst case")
        elif b:
            print("best case")
            print(min(s))
        if((w==True and b==True)or(w==False and b==False)):
            for i in range (n):
                if(s[i]>59):
                    print(s[i-1])
                    break
            for i in range (n):
                if(s[i]>59):
                    print(s[i])
                    break
    except EOFError:
        break
