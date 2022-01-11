"""n 個の整数 a[0],a[1],…,a[n−1]が与えられる。
これらの整数から何個かの整数を選んで総和をとったときの、総和の最大値を求めよ。
また、何も選ばない場合の総和は 0 であるものとする。
"""

n = int(input())
a = list(map(int, input().split()))

#dpテーブル
dp = [0] * (n + 1)
#print(dp)

#dp処理
for i in range(n):
    dp[i + 1] = max(dp[i], dp[i] + a[i])
    print(dp)
print(dp[-1])
