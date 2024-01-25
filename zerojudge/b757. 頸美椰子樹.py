while True:
    try:
        r=float(input())
        print("%g" %((r*9)/5+32))
    except EOFError:
        break