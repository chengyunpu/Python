while True:
    try:
        n=float(input())
        print("|%.4f|=%.4f"%(n,abs(n)))
    except:
        break