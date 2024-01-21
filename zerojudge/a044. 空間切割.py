while True:
        try:
                n=int(input())
                print(int(((n+1)*((n*n)-n+6))/6))
        except EOFError:
                break