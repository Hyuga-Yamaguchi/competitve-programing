q = int(input())
s, t = [], []
for i in range(2 * q):
    if i % 2 == 0:
        s.append(input())
    else:
        t.append(input())
#print(s, t)
for k in range(q):
    ls, lt = len(s[k]), len(t[k])
    dp = [[0] * (lt + 1) for _ in range(ls+ 1)]
    dp[0][0] = 0
    for i in range(ls):
        for j in range(lt):
            if s[k][i] == t[k][j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    print(dp[ls][lt])
