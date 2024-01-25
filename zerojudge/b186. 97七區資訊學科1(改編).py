while True:
    try:
        a,b,c=map(int,input().split())
        n=min(a//10,c//2)
        print("%d 個餅乾，%d 盒巧克力，%d 個蛋糕。"%(a,b+n,c))
    except EOFError:
        break