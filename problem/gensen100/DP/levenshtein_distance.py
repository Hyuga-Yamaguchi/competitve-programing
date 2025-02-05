"""
問題 10:　レーベンシュタイン距離 (diffコマンド)
2つの文字列S,Tが与えられます。
Sに以下の3種類の操作のいずれかを順次実施して Tに変換したいです。
そのような一連の操作のうち、操作回数の最小値を求めよ。

(操作)
＜変更＞ Sの中から文字S[i]を1個選んで、その文字を好きな文字に変更します。
＜削除＞ Sの中から文字S[i]を1個選んで、その文字を削除します。
＜挿入＞ Sの好きな箇所に好きな文字を挿入します。

【制約】
・ 1≤|S|,|T|≤1000
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j + 1] = dp[i][j] + 1
        if j == 0:
            dp[i + 1][j] = dp[i][j] + 1

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
        else:
            dp[i + 1][j + 1] = min(dp[i][j] + 1, dp[i + 1][j] + 1, dp[i][j + 1] + 1)
print(dp[n][m])
