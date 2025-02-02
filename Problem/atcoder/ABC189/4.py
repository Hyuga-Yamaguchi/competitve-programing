n = int(input())
s = list(input() for _ in range(n))
s = s[::-1]
#print(s)

dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(2):
        if j == 0:
            if s[i] == "OR":
                dp[i + 1][0] += dp[i][0] * 2
                dp[i + 1][1] += dp[i][0]
            elif s[i] == "AND":
                dp[i + 1][0] += dp[i][0]
        elif j == 1:
            if s[i] == "OR":
                dp[i + 1][1] += dp[i][1]
            elif s[i] == "AND":
                dp[i + 1][0] += dp[i][1]
                dp[i + 1][1] += dp[i][1] * 2
#print(dp)
print(dp[n][0] + dp[n][1])
