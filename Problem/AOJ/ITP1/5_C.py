while True:
    h, w = map(int, input().split())
    if (h, w) == (0, 0):
        break
    s = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                if j % 2 == 0:
                    s[i][j] = "#"
                else:
                    s[i][j] = "."
            else:
                if j % 2 == 0:
                    s[i][j] = "."
                else:
                    s[i][j] = "#"
    for i in range(h):
        ans = ""
        for j in range(w):
            ans += s[i][j]
        print(ans)
    print("")
