while True:
    try:
        a, b, c = map(str, input().split())
        if b == '/':
            print(int(a) // int(c))
        elif b == '+':
            print(int(a) + int(c))
        elif b == '-':
            print(int(a) - int(c))
        else:
            print(int(a) * int(c))

    except EOFError:
        break