import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
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

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    t = int_list()
    sum_t = sum(t)

    A = 101010

    dp = [[False] * (A + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(A + 1):
            dp[i + 1][j] |= dp[i][j]
            if j >= t[i]:
                dp[i + 1][j] |= dp[i][j - t[i]]

    ans = INF
    for i in range(A):
        if dp[n][i] and sum_t - i <= i:
            ans = min(ans, i)
    print(ans)

if __name__ == '__main__':
    main()
