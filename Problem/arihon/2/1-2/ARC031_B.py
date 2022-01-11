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
def str_input(): return input().strip()
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
    a = str_row_list(10)
    #print(a)
    b = deepcopy(a)

    def dfs(y, x):
        seen[y][x] = True

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = y + dy; nx = x + dx
            if not 0 <= ny < 10 or not 0 <= nx < 10:
                continue
            if a[ny][nx] == "x":
                continue
            if seen[ny][nx]:
                continue
            dfs(ny, nx)

    flag = False
    for i in range(10):
        for j in range(10):
            a = deepcopy(b)
            a[i][j] = "o"
            #print(a)
            seen = [[False] * 10 for _ in range(10)]
            cnt = 0
            for k in range(10):
                for l in range(10):
                    if seen[k][l]:
                        continue
                    if a[k][l] == "o":
                        dfs(k, l)
                        cnt += 1
            if cnt == 1:
                flag = True
    #print(cnt_lis)
    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
