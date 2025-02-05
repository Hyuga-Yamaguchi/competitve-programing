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
    r, c, k = int_map()
    grid = [[0] * (c + 1) for _ in range(r + 1)]
    for i in range(k):
        x, y, v = int_map()
        grid[x][y] = v
    #print(grid)

    dp = [[[0] * 4 for _ in range(c + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(c + 1):
            for k in range(4):
                if i - 1 >= 0:
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][k])
                    dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][k] + grid[i][j])
                if j - 1 >= 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])
                    if k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + grid[i][j])

    ans = 0
    for k in range(4):
        ans = max(ans, dp[-1][-1][k])
    print(ans)

if __name__ == '__main__':
    main()
