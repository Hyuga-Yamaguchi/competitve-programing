import sys, re
# from math import ceil, floor, sqrt, pi, factorial, gcd
# from copy import copy, deepcopy
from collections import Counter, deque
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
def str_input(): return input()[:-1]
# def str_map(): return input().split()
# def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
#def str_row_list(N): return [list(str_input()) for _ in range(N)]
# def lcm(a, b): return a * b // gcd(a, b)
# sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
# MOD = 10 ** 9 + 7
# mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
h, w = int_map()
c = str_row(h)

def bfs(sy, sx):
    q = deque()
    q.append([sy, sx])
    dist[sy][sx] = 0
    #print(q)
    while q:
        [y, x] = q.popleft()
        for (dy, dx) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = y + dy; nx = x + dx
            if not 0 <= ny < h or not 0 <= nx < w:
                continue
            if dist[ny][nx] != INF: #append, appendleftで距離順に探索できるのでINFの比較でOK
                continue
            if c[ny][nx] == "#":
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])
            else:
                dist[ny][nx] = dist[y][x]
                q.appendleft([ny, nx])
            print(dist)

dist = [[INF] * w for _ in range(h)]

sy = 0; sx = 0; gy = 0; gx = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sy = i; sx = j
        if c[i][j] == "g":
            gy = i; gx = j

bfs(sy, sx)
#print(dist)
if dist[gy][gx] <= 2:
    print("YES")
else:
    print("NO")
