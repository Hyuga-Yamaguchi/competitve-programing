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
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

ans = 0
def main():
    m = int_input()
    n = int_input()
    c = int_row_list(n)
    #print(c)

    def dfs(x, y, d):
        global ans
        if not (0 <= x < n) or not (0 <= y < m) or c[x][y] == 0:
            return 0

        c[x][y] = 0
        dfs(x + 1, y, d + 1)
        dfs(x - 1, y, d + 1)
        dfs(x, y + 1, d + 1)
        dfs(x, y - 1, d + 1)
        c[x][y] = 1
        ans = max(ans, d)

    for i in range(n):
        for j in range(m):
            dfs(i, j, 1)
    print(ans)

if __name__ == '__main__':
    main()
