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
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = int_map()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    def bfs(graph, start, n):
        queue = deque([start])
        dist = [None] * n # uからの距離の初期化
        dist[start] = 0 # 自分との距離は0
        cnt = [0] * n
        cnt[0] = 1 #通過した道の本数
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if dist[i] is None:
                    dist[i] = dist[v] + 1
                    queue.append(i)
                    cnt[i] = cnt[v]
                elif dist[i] == dist[v] + 1:
                    cnt[i] += cnt[v] % MOD
        return dist

    d = bfs(g, 0, n)
    point = 0; idx = 0
    for i in range(n):
        if point <= d[i]:
            point = d[i]
            idx = i
    #print(idx)
    d2 = bfs(g, idx, n)
    print(max(d2) + 1)


if __name__ == '__main__':
    main()
