while True:
    try:
        w=int(input())
        h=float(input())
        print("%.1f"%(w/(h*h)))
    except EOFError:
        break