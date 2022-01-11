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
    while True:
        w, h = int_map()
        c = int_row_list(h)
        if (w, h) == (0, 0):
            break

        def dfs(y, x):
            c[y][x] = 0

            for (dy, dx) in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                ny = y + dy; nx = x + dx
                if not 0 <= ny < h or not 0 <= nx < w:
                    continue
                if c[ny][nx] == 0:
                    continue
                dfs(ny, nx)

        seen = [[False] * w for _ in range(h)]

        cnt = 0
        for i in range(h):
            for j in range(w):
                if c[i][j] == 0:
                    continue
                dfs(i, j)
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()
