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
number_start = 48 #"0"のASCIIコード

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    point = [None] * (n - 1)
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = int_map()
        if i <= n - 2:
            point[i] = [a - 1, b - 1]
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    depth = [0] * n
    def dfs1(g, v, p = -1, dist = 0):
        depth[v] = dist
        for c in g[v]:
            if c == p:
                continue
            dfs1(g, c, v, dist + 1)
    dfs1(g, 0)
    #print(depth)

    q = int_input()
    value = [0] * n
    for i in range(q):
        t, e, x = int_map()
        e -= 1
        if t == 1:
            start = point[e][0]
            goal = point[e][1]
        elif t == 2:
            start = point[e][1]
            goal = point[e][0]
        if depth[start] < depth[goal]:
            value[0] += x
            value[goal] -= x
        else:
            value[start] += x
    #print(value)

    def dfs(g, v, p = -1, cost = 0):
        value[v] += cost
        for c in g[v]:
            if c == p:
                continue
            dfs(g, c, v, value[v])
    dfs(g, 0)
    for ans in value:
        print(ans)

if __name__ == '__main__':
    main()
