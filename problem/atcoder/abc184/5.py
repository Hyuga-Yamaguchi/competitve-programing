import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np
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
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード

h, w = int_map()

def bfs(sy, sx, c, u):
    global h, w
    dist = [[INF] * w for _ in range(h)]
    queue = deque([[sy, sx]])
    dist[sy][sx] = 0
    while queue:
        [y, x] = queue.popleft()
        dist2 = dist[y][x] + 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if not 0 <= ny < h or not 0 <= nx < w:
                continue
            if c[ny][nx] == "#":
                continue
            if dist[ny][nx] > dist2:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
        if c[y][x].islower():
            t = ord(c[y][x]) - 97
            for y_, x_ in u[t]:
                if dist[y_][x_] > dist2:
                    dist[y_][x_] = dist2
                    queue.append((y_, x_))
            u[t].clear()
    return dist

#メモリ消費を抑える時はグローバル空間に書く
def main():
    a = str_row(h)

    tele = [[] for i in range(26)]
    for i in range(h):
        for j in range(w):
            if a[i][j].islower():
                tele[ord(a[i][j]) - 97].append((i, j))
            elif a[i][j] == "S":
                sy = i; sx = j
            elif a[i][j] == "G":
                gy = i; gx = j
    #print(tele)

    dist = bfs(sy, sx, a, tele)
    if dist[gy][gx] == INF:
        print(-1)
    else:
        print(dist[gy][gx])


if __name__ == '__main__':
    main()
