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
def str_row_list(N): return [list(str_input()) for _ in range(N)]
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
    n = int_input()
    a = int_list()
    b = int_list()

    ab = [None] * n
    for i in range(n):
        ab[i] = (a[i], b[i])

    ab.sort(key = itemgetter(0))

    #bの部分和:maxAが5000なので5000まで考えれば良い
    MAX = 5001
    dp = [[0] * MAX for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(MAX):
            b_i = ab[i][1]
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
            if j + b_i <= MAX - 1:
                dp[i + 1][j + b_i] += dp[i][j]
                dp[i + 1][j + b_i] %= mod
    #print(dp)

    #各行ごとで累積和をとる
    dp_ = [[0] * MAX for _ in range(n + 1)]
    for i in range(n + 1):
        dp_[i][0] = dp[i][0]
        dp_[i][0] %= mod
        for j in range(1, MAX):
            dp_[i][j] = dp_[i][j - 1] + dp[i][j]
            dp_[i][j] %= mod
    #print(dp_)

    ans = 0
    for i in range(n):
        a = ab[i][0]; b = ab[i][1]
        if a < b:
            continue
        sa = a - b
        ans += dp_[i][sa]
        ans %= mod
    print(ans)




if __name__ == '__main__':
    main()
