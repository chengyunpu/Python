while True:
    try:
        a=str(input())
        b=str(input())
        c=str(input())
        print("%s%s和%s絕交" %(a,"想"if c=="yes" else "不想",b))
    except EOFError:
        break