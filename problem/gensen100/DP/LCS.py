"""
最長共通部分列 (LCS) 問題
2つの文字列S,Tが与えられる。
"abcde" といった文字列の部分文字列とは、"a", "ad", "abe" といったように、
文字列から文字を幾つか抜き出して順に繋げてできる文字列のことを言うものとする。
このとき、SとTの共通の部分文字列となる文字列の長さの最大値を求めよ。
【制約】
・ 1≤|S|,|T|≤1000
"""
s = input()
t = input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
dp[0][0] = 0

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
print(dp)
print(dp[len(s)][len(t)])


"""
dp[i + 1][j + 1]:= Sのi文字目までとTのj文字目まででのLCSの長さ
とします。
dp[i][j], dp[i + 1][j], dp[i][j + 1]を使って dp[i + 1][j + 1]を表すことを考えると次のようになります。

S[i]==T[j]ならば、dp[i][j]に対して、共通のSのi文字目とTのj文字目を付け加えれば1文字伸びるので、
dp[i + 1][j + 1]=dp[i][j] + 1
dp[i+1][j]に対して、Tのj文字目を考慮しても特にLCSの長さは変わらず、
dp[i + 1][j + 1]=dp[i + 1][j]
dp[i][j+1]に対して、Sのi文字目を考慮しても特にLCSの長さは変わらず、
dp[i + 1][j + 1]=dp[i][j + 1]
まとめると、

＜DP漸化式＞

dp[i + 1][j + 1] = max(dp[i][j] + 1,dp[i + 1][j], dp[i][j + 1])(S[i] == T[j])
dp[i + 1][j + 1] = max(dp[i + 1][j],dp[i][j + 1])(S[i] != T[j])
＜DP初期条件＞
dp[0][0] = 0
＜求める値＞
dp[|S|][|T|]
"""
