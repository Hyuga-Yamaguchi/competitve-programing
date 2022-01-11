"""
2つの文字列S, Tが与えられる。
Sには以下の３通りの操作を繰り返すことで、Tに変換したいものとする。
そのような操作の一連で、操作回数の最小回数を求めよ。
 *変更：S中の文字から１つ選んで任意の文字に変更する
 *削除：S中の文字を１つ選んで削除する
 *挿入:Sの好きな箇所に好きな文字を１文字挿入する
"""

def chmin(a, b):
    if a > b:
        a = b
    return a

INF = 2 * 29

s = input()
t = input()

ls = len(s)
lt = len(t)

#DPテーブル処理
dp = [[INF] * (lt + 1) for i in range(ls + 1)]

#初期条件
dp[0][0] = 0

#DPループ
for i in range(ls + 1):
    for j in range(lt + 1):
        #変更操作
        if i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)
        #削除操作
        if i > 0:
            dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)
        #挿入操作
        if j > 0:
            dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)

print(dp)
print(dp[ls][lt])
