import sys, re
# from math import ceil, floor, sqrt, pi, factorial, gcd
# from copy import copy, deepcopy
# from collections import Counter, deque
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, product, combinations, combinations_with_replacement
# from bisect import bisect, bisect_left, bisect_right
# from functools import reduce
# from decimal import Decimal, getcontext
# from operator import itemgetter
#import numpy as np #pypyでは使用不可
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
# def int_list(): return list(int_map())
# def int_row(N): return [int_input() for _ in range(N)]
# def int_row_list(N): return [int_list() for _ in range(N)]
def str_input(): return input()
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_input()) for _ in range(N)]
# def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
#flaot_INF = float('inf')
#INF = 1 << 60
#MOD = 10 ** 9 + 7

h, w = int_map()
C = str_row_list(h)
#print(C)

def dfs(y, x):
    seen[y][x] = True

    #探索
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        #範囲外に行ったらreturn
        if not 0 <= ny < h or not 0 <= nx < w:
            continue
        #壁に当たったらreturn
        if C[ny][nx] == "#":
            continue
        if seen[ny][nx]:
            continue
        dfs(ny, nx)

sx = 0; sy = 0; gx = 0; gy = 0
for i in range(h):
    for j in range(w):
        if C[i][j] == "s":
            sx = j; sy = i
        if C[i][j] == "g":
            gx = j; gy = i
seen = [[False] * w for _ in range(h)]
dfs(sy, sx)
if seen[gy][gx]:
    print("Yes")
else:
    print("No")
