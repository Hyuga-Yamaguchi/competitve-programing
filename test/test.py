"""
ある銀行では、お金の引き出しを難しくするために、一回の操作で引き出せる金額が以下のいずれかとなっています。
・1円
・6円、6^2(=36)円、6^3(=216)円、...
・9円、9^2(=81)円、9^3(=729)円、...
この銀行からちょうどN円を引き出すには少なくとも何回の操作が必要か求めてください。
ただし、一度引き出したお金を再び預け入れてはならないとします。
"""
import time
import sys
#1円から順に解く最小化問題
import math
N = int(input())
t1 = time.time()

#indexが金額、dp[i]が引き出し回数 （配る配列なので数に余裕を）
dp = [math.inf] * (N + 10)
dp[0] = 0
print(sys.getsizeof(dp))

for i in range(N+1):
    dp[i+1] = min(dp[i+1], dp[i]+1)

    for j in range(1, 7):    # 金額iから +6^j or +9^j 円の引き出し回数を計算
        if i+pow(6, j) <= N: # 配る先の金額がNを超えてなければ i + 6^j 円の計算
            dp[i+pow(6, j)] = min(dp[i+pow(6, j)], dp[i]+1)
        if i+pow(9, j) <= N: # 配る先の金額がNを超えてなければ i + 9^j 円の計算
            dp[i+pow(9, j)] = min(dp[i+pow(9, j)], dp[i]+1)


# for i in range(N+1):
#      print(str(i) + "\t" + str(dp[i]))
t2 = time.time()
print(dp[N])
print(t2 - t1)
