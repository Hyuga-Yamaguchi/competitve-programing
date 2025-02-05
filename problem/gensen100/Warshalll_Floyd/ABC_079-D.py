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
def str_input(): return input()
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
flaot_INF = float('inf')
INF = 1 << 60
MOD = 10 ** 9 + 7

def main():
    H, W = int_map() #頂点数, 辺数
    c = []
    for i in range(10):
        C = int_list()
        c.append(C)
    #print(c)

    dp = [[INF] * 10 for _ in range(10)]

    for i in range(10):
        for j in range(10):
            dp[i][j] = c[i][j]
    for v in range(10):
        dp[v][v] = 0

    #dp遷移(ワーシャルフロイド法)
    for k in range(10):
        for i in range(10):
            for j in range(10):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    #print(dp)

    ans = 0
    for i in range(H):
        a = int_list()
        for j in range(W):
            if a[j] == -1:
                continue
            ans += dp[a[j]][1]
    print(ans)


if __name__ == '__main__':
    main()
