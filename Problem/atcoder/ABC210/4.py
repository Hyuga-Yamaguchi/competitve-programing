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

#メモリ消費を抑える時はグローバル空間に書く
def main():
    h, w, c = int_map()
    a = int_row_list(h)
    b = [[None] * h for _ in range(w)] #90°反転
    for i in range(w):
        for j in range(h):
            b[i][j] = a[abs(h - 1 - j)][i]
    #print(b)

    matrix_1 = [[None] * w for _ in range(h)]
    matrix_2 = [[None] * w for _ in range(h)]
    matrix_3 = [[None] * h for _ in range(w)]
    matrix_4 = [[None] * h for _ in range(w)]

    #ぐりっどそのまま
    for i in range(h):
        for j in range(w):
            matrix_1[i][j] = a[i][j] - c * (i + j)
            matrix_2[i][j] = a[i][j] + c * (i + j)
    #print(matrix_1)
    #最小化
    dp = [[INF] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i == 0 and j >= 1:
                dp[i][j] = min(dp[i][j], dp[i][j - 1], matrix_1[i][j - 1])
            if i >= 1 and j == 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j], matrix_1[i - 1][j])
            if i >= 1 and j >= 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j], dp[i][j - 1], matrix_1[i - 1][j], matrix_1[i][j - 1])
    #print(dp)

    ans1 = INF
    for i in range(h):
        for j in range(w):
            ans1 = min(ans1, dp[i][j] + matrix_2[i][j])
    #print(ans1)

    #グリッド90°回転
    #ぐりっどそのまま
    for i in range(w):
        for j in range(h):
            matrix_3[i][j] = b[i][j] - c * (i + j)
            matrix_4[i][j] = b[i][j] + c * (i + j)

    dp_ = [[INF] * h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            if i == 0 and j >= 1:
                dp_[i][j] = min(dp_[i][j], dp_[i][j - 1], matrix_3[i][j - 1])
            if i >= 1 and j == 0:
                dp_[i][j] = min(dp_[i][j], dp_[i - 1][j], matrix_3[i - 1][j])
            if i >= 1 and j >= 1:
                dp_[i][j] = min(dp_[i][j], dp_[i - 1][j], dp_[i][j - 1], matrix_3[i - 1][j], matrix_3[i][j - 1])
    #print(dp_)

    ans2 = INF
    for i in range(w):
        for j in range(h):
            ans2 = min(ans2, dp_[i][j] + matrix_4[i][j])
    #print(ans2)

    print(min(ans1, ans2))

if __name__ == '__main__':
    main()
