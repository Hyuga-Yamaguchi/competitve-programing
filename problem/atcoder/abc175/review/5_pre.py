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
    grid = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(K):
        r, c, v = int_map()
        grid[r][c] = v
    #print(g)

    dp = [[[0] * 4 for _ in range(C + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(C + 1):
            for k in range(4):
                if i - 1 >= 0:
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][k])
                    dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][k] + grid[i][j])
                if j - 1 >= 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])
                    if k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + grid[i][j])

    for i in range(R + 1):
        print(dp[i])

    ans = 0
    for k in range(4):
        ans = max(ans, dp[-1][-1][k])
    print(ans)

if __name__ == '__main__':
    main()
