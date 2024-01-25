while True:
    try:
        h,d=map(int,input().split())
        print(2*(h+d))
    except EOFError:
        break