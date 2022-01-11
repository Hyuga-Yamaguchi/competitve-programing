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
    n = int_input()
    a = int_list()

    dp = [[0] * 10 for _ in range(n)]
    f0 = (a[0] + a[1]) % 10
    g0 = (a[0] * a[1]) % 10
    dp[0][f0] += 1; dp[0][g0] += 1

    for i in range(1, n - 1):
        for j in range(10):
            if dp[i - 1][j] > 0:
                dp[i][(j + a[i + 1]) % 10] += dp[i - 1][j]
                dp[i][(j + a[i + 1]) % 10] %= mod
                dp[i][(j * a[i + 1]) % 10] += dp[i - 1][j]
                dp[i][(j * a[i + 1]) % 10] %= mod
    #print(dp)

    for i in range(10):
        print(dp[-2][i] % mod)

if __name__ == '__main__':
    main()
