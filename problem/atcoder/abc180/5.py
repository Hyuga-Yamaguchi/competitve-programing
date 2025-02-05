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
    x = [None] * n; y = [None] * n; z = [None] * n
    for i in range(n):
        X, Y, Z = int_map()
        x[i] = X; y[i] = Y; z[i] = Z

    dist = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = abs(x[i] - x[j]) + abs(y[i] - y[j]) + max(0, z[i] - z[j])
    #print(dist)

    dp = [[INF] * (n + 1) for _ in range((1 << n) + 1)]
    dp[0][0] = 0

    for S in range(1 << n):
        for v in range(n):
            for u in range(n):
                if S != 0 and not (S & (1 << u)):
                    continue #uを含まない場合を除く
                if (S & (1 << v)) == 0:
                    dp[S | (1 << v)][v] = min(dp[S | (1 << v)][v], dp[S][u] + dist[u][v])

    #print(dp)

    if dp[(1 << n) - 1][0] != INF:
        print(dp[(1 << n) - 1][0])
    else:
        print(-1)


if __name__ == '__main__':
    main()
