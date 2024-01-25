while True:
    try:
        s = input().replace(" ", "")  # 刪除空白
        n = len(s)
        k = 0

        if s == '0':
            break

        for i in range(n):
            if 'A' <= s[i] <= 'Z':
                k += ord(s[i]) - ord('A') + 1
            elif 'a' <= s[i] <= 'z':
                k += ord(s[i]) - ord('a') + 1
            else:
                print("Fail")
                break

        # 在只印出總和時加上條件判斷
        if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
            print(k)

    except EOFError:
        break
