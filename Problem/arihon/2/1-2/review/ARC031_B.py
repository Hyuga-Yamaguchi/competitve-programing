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
    a = str_row_list(10)
    #print(a)

    def dfs(y, x):
        seen[y][x] = True

        for (dy, dx) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = y + dy; nx = x + dx
            if not 0 <= ny < 10 or not 0 <= nx < 10:
                continue
            if a[ny][nx] == "x":
                continue
            if seen[ny][nx]:
                continue
            dfs(ny, nx)

    o_cnt = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] == "o":
                o_cnt += 1
    #print("o_cnt", o_cnt)

    for i in range(10):
        for j in range(10):
            if a[i][j] == "o":
                flag = False
            else:
                flag = True

            a[i][j] = "o"
            seen = [[False] * 10 for _ in range(10)]
            dfs(i, j)

            cur_o_cnt = 0
            for k in range(10):
                for l in range(10):
                    if seen[k][l]:
                        cur_o_cnt += 1

            #print("cur_o_cnt", cur_o_cnt)
            if o_cnt + 1 == cur_o_cnt:
                print("YES")
                exit()

            if flag:
                a[i][j] = "x"

    print("NO")



if __name__ == '__main__':
    main()
