"""
N個の整数a[0], a[1], ・・・、a[N-1]と、N個の整数b[0], b[1], ・・・, b[N-1]が与えられる。
2組の整数列からそれぞれ１個ずつ選んで和をとる
その和として考えられる値のうち、整数K以上の範囲内での最小値を求めよ
"""

"""
N個の正の整数b[0], b[1], ・・・, b[N-1]が与えられる。
このうちK - a[i]以上の範囲内での最小値を求める。
"""
import bisect

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#暫定最小値を格納する変数
INF = 2 * (10 ** 8)
min_value = INF

#bをソート
b = sorted(b)

#aを固定して解く
for i in range(N):
    #bのなかでK - a[i]以上の範囲での最小値を示すイテレータ
    # bisect_left := A[i] < x となる i の個数(インデックスではないので注意)
    iter = bisect.bisect_left(b, K - a[i])
    #イテレータの示す値を取り出す
    val = b[iter]
    #min_valueと比較する
    if a[i] + val < min_value:
        min_value = a[i] + val

print(min_value)
