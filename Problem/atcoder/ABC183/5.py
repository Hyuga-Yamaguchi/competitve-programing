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
#import numpy as np #pypyでは使用不可
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
    h, w = int_map()
    s = str_row(h)

    #横の累積和
    x = [[0] * w for _ in range(h)]
    x[0][0] = 0
    #縦の累積和
    y = [[0] * w for _ in range(h)]
    y[0][0] = 0
    #斜めの累積和
    z = [[0] * w for _ in range(h)]
    z[0][0] = 0

    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                dp[i][j] = 0
            elif i == 0 and j >= 1:
                dp[i][j] = (dp[i][j - 1] + x[i][j - 1]) % MOD
                x[i][j] = (dp[i][j - 1] + x[i][j - 1]) % MOD
            elif i >= 1 and j == 0:
                dp[i][j] = (dp[i - 1][j] + y[i - 1][j]) % MOD
                y[i][j] = (dp[i - 1][j] + y[i - 1][j]) % MOD
            elif i >= 1 and j >= 1:
                dp[i][j] = (dp[i][j - 1] + x[i][j - 1] + dp[i - 1][j] + y[i - 1][j] + dp[i - 1][j - 1] + z[i - 1][j - 1]) % MOD
                x[i][j] = (dp[i][j - 1] + x[i][j - 1]) % MOD
                y[i][j] = (dp[i - 1][j] + y[i - 1][j]) % MOD
                z[i][j] = (dp[i - 1][j - 1] + z[i - 1][j - 1]) % MOD

    #print("dp", dp)
    #print("x", x)
    #print("y", y)
    #print("z", z)
    print(dp[-1][-1] % MOD)


if __name__ == '__main__':
    main()
