# 内包表記
data = range(1, 10)
count = len([x for x in data if x % 3 == 0]) # 3の倍数をカウント
print(count)

# 累積和
from itertools import accumulate
a = list(range(1, 11))
b = list(accumulate(a))     # itertoolsの戻り値はイテレータとなっているので必要に応じてlist化します．
print(a)
print(b)

# リスト操作
a = [1, 2, 3, 4, 5]
del a[1]        # インデックス指定で削除したい場合
print(a)

b = [1, 2, 3, 4, 5]
del b[1:3]      # スライスで部分リストを指定して削除も可能
print(b)

c = [1, 2, 3, 4, 5]
x = c.pop(1)    # popでもインデックス指定で削除可能
print(c, x)

d = [1, 2, 3, 4, 5]
d.remove(3)     # オブジェクトを指定して削除したい場合
print(d)

# n進数
print(bin(255))                 # 10進数 -> 2進数
print(hex(255))                 # 10進数 -> 16進数

print(int('0b11111111', 2))     # 2進数 -> 10進数
print(int('0xff', 16))          # 16進数 -> 10進数

# 階乗
from math import factorial
def permutations_count(n, r):
    return factorial(n) // factorial(n - r)
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
print(permutations_count(5, 2))
print(combinations_count(5, 2))

# 二分探索
import bisect
"""
bisect_left と　lower_bound　は同じ
//ソート済みの配列aにおいて、a[i] >= key という条件を満たす最小の添字iを返す
//ソート済みの配列aにおいて、a[i] < key　という条件を満たす配列の個数を返す
"""
n = bisect.bisect_left(A, x)  # A[i] < x となる i の個数
n = bisect.bisect_right(A, x)  # A[i] <= x となる i の個数

import numpy as np
n = np.searchsorted(A, x, side='left')
n = np.searchsorted(A, x, side='right')  # A[i] <= x となる i の個数
