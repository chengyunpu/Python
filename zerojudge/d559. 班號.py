while True:
    try:
        s=str(input())
        print("'C' can use printf(\"%d\",n); to show integer like " + s)
    except EOFError:
        break