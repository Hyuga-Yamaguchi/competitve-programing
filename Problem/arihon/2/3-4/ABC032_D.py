import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
def str_input(): return input()[:-1]
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, W = int_map()
    value = [None] * n; weight = [None] * n
    for i in range(n):
        v, w = int_map()
        value[i] = v; weight[i] = w

    def half_bit_search(l, r):
        value_ = value[l:r]; weight_ = weight[l:r]
        n = len(value_)
        cnd = [None] * (1 << n)
        for bit in range(1 << n):
            va = 0; we = 0
            for i in range(n):
                if bit & (1 << i):
                    va += value_[i]
                    we += weight_[i]
            cnd[bit] = (va, we)
        return cnd

    if max(value) > 1000 and max(weight) > 1000:
        cnd1 = half_bit_search(0, n // 2)
        cnd2 = half_bit_search(n // 2, n)
        cnd1.sort(key = itemgetter(1))

        ans = 0
        for (va, we) in cnd2:
            left = 0; right = len(cnd2)
            while right - left > 1:
                mid = (right + left) // 2
                if we + cnd1[mid][1] <= W:
                    ans = max(ans, va + cnd1[mid][0])
                    left = mid
                else:
                    right = mid
        print(ans)

    elif max(weight) <= 1000:
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(W + 1):
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
                if j + weight[i] <= W:
                    dp[i + 1][j + weight[i]] = max(dp[i][j] + value[i], dp[i + 1][j + weight[i]])
        print(dp[-1][-1])

    else:
        V = sum(value)
        dp = [[INF] * (V + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(V + 1):
                dp[i + 1][j] = dp[i][j]
                if j >= value[i]:
                    dp[i + 1][j] = min(dp[i][j - value[i]] + weight[i], dp[i + 1][j])
        #print(dp[-1])

        idx = 0
        for j in range(V + 1):
            if dp[-1][j] <= W:
                idx = j
        print(idx)

if __name__ == '__main__':
    main()
