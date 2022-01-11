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
    V, E = int_map() #頂点数, 辺数

    dp = [[INF] * V for _ in range(V)]

    for e in range(E):
        a, b, w = int_map()
        dp[a - 1][b - 1] = w
        dp[b - 1][a - 1] = w
    for v in range(V):
        dp[v][v] = 0

    #dp遷移(ワーシャルフロイド法)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    #print(dp)
    ans = INF
    for i in range(V):
        tmp = 0
        for j in range(V):
            if dp[i][j] <=  0:
                continue
            tmp = max(dp[i][j], tmp)
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
