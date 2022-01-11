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
def str_row_list(N): return [list(str_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    R, C, K = int_map()
    g = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(K):
        r, c, v = int_map()
        g[r][c] = v
    print(g)

    dp = [[[0] * (C + 1) for _ in range(R + 1)] for _ in range(4)]

    for i in range(R + 1):
        for j in range(C + 1):
            for k in range(4):
                #行の遷移
                if i + 1 <= R:
                    #(i + 1, j)のアイテムを拾わない場合
                    #i + 1行目で拾ったアイテムは0個なので、k = 0を更新する
                    dp[0][i + 1][j] = max(dp[0][i + 1][j], dp[k][i][j])
                    #(i + 1, j)のアイテムを拾う場合
                    #i + 1行目で拾ったアイテムは１個なので、k = 1を更新する
                    dp[1][i + 1][j] = max(dp[1][i + 1][j], dp[k][i][j] + g[i + 1][j])
                #列の遷移
                if j + 1 <= C:
                    #(i, j + 1)のアイテムを拾わない場合
                    dp[k][i][j + 1] = max(dp[k][i][j + 1], dp[k][i][j])
                    #(i, j + 1)のアイテムを拾う場合
                    if k < 3:
                        dp[k + 1][i][j + 1] = max(dp[k + 1][i][j + 1], dp[k][i][j] + g[i][j + 1])

    print(dp)
    ans = 0
    for k in range(4):
        ans = max(ans, dp[k][-1][-1])
    print(ans)

if __name__ == '__main__':
    main()
