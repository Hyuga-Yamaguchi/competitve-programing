import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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
    h, w = int_map()
    a = []
    for i in range(h):
        A = str_input()
        a.append(A)
    #print(a)

    dp = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 0:
                dp[i][j] = -INF
            else:
                dp[i][j] = INF
    #print(dp)
    dp[h - 1][w - 1] = 0

    for i in range(h):
        i = h - i - 1
        for j in range(w):
            j = w - j - 1
            if (i + j) % 2 == 0:
                if a[i][j] == "-":
                    if i - 1 >= 0:
                        dp[i - 1][j] = min(dp[i - 1][j], dp[i][j] + 1)
                    if j - 1 >= 0:
                        dp[i][j - 1] = min(dp[i][j - 1], dp[i][j] + 1)
                else:
                    if i - 1 >= 0:
                        dp[i - 1][j] = min(dp[i - 1][j], dp[i][j] - 1)
                    if j - 1 >= 0:
                        dp[i][j - 1] = min(dp[i][j - 1], dp[i][j] - 1)
            else:
                if a[i][j] == "-":
                    if i - 1 >= 0:
                        dp[i - 1][j] = max(dp[i - 1][j], dp[i][j] - 1)
                    if j - 1 >= 0:
                        dp[i][j - 1] = max(dp[i][j - 1], dp[i][j] - 1)
                else:
                    if i - 1 >= 0:
                        dp[i - 1][j] = max(dp[i - 1][j], dp[i][j] + 1)
                    if j - 1 >= 0:
                        dp[i][j - 1] = max(dp[i][j - 1], dp[i][j] + 1)
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")


if __name__ == '__main__':
    main()
