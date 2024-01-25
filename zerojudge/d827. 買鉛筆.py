while True:
    try:
        n=int(input())
        print((n//12)*50+(n%12)*5)
    except EOFError:
        break