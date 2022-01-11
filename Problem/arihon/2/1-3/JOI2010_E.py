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
    h, w, n = int_map()
    c = str_row(h)

    def bfs(sy, sx, gy, gx):
        q = deque()
        q.append([sy, sx])
        dist = [[INF] * w for _ in range(h)]
        dist[sy][sx] = 0
        while q:
            [y, x] = q.popleft()
            for (dy, dx) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if not 0 <= ny < h or not 0 <= nx < w:
                    continue
                if c[ny][nx] == "X":
                    continue
                if dist[ny][nx] != INF:
                    continue
                q.append([ny, nx])
                dist[ny][nx] = dist[y][x] + 1
        return dist[gy][gx]

    point = []
    for i in range(n + 1):
        if i == 0:
            for j in range(h):
                for k in range(w):
                    if c[j][k] == "S":
                        point.append([j, k])
        else:
            for j in range(h):
                for k in range(w):
                    if c[j][k] == str(i):
                        point.append([j, k])
    #print(point)

    ans = 0
    for i in range(len(point) - 1):
        sy, sx = point[i][0], point[i][1]
        gy, gx = point[i + 1][0], point[i + 1][1]
        ans += bfs(sy, sx, gy, gx)
    print(ans)

if __name__ == '__main__':
    main()
