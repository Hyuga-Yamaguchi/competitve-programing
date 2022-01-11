n = int(input())
s = [[None] * n for _ in range(5)]
for i in range(5):
    S = input()
    for j in range(n):
        s[i][j] = S[j]
#print(s)

INF = 10 ** 9
dp = [[INF] * 3 for _ in range(n)]

def COUNT(x):
    count = [0] * 3
    for i in range(5):
        if s[i][x] == "R":
            count[0] += 1
        elif s[i][x] == "B":
            count[1] += 1
        elif s[i][x] == "W":
            count[2] += 1
    return count

dp[0][0] = 5 - COUNT(0)[0]
dp[0][1] = 5 - COUNT(0)[1]
dp[0][2] = 5 - COUNT(0)[2]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1] + 5 - COUNT(i)[0], dp[i - 1][2] + 5 - COUNT(i)[0])
        elif j == 1:
            dp[i][j] = min(dp[i - 1][0] + 5 - COUNT(i)[1], dp[i - 1][2] + 5 - COUNT(i)[1])
        elif j == 2:
            dp[i][j] = min(dp[i - 1][0] + 5 - COUNT(i)[2], dp[i - 1][1] + 5 - COUNT(i)[2])
print(min(dp[n - 1]))
