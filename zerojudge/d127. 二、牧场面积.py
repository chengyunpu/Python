while True:
    try:
        n=int(input())
        print((n//4)*(n//4+(n%4!=0)))
    except EOFError:
        break