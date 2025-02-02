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
def str_row_list(N): return [list(str_map()) for _ in range(N)]
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
    n, k = int_map()
    p = int_list()
    c = int_list()

    g = [[] for _ in range(n)]

    for i in range(n):
        g[p[i] - 1].append(p[p[i] - 1] - 1)
    # print(g)

    def dfs(g, v, start, now, score):
        now += c[v]
        score.append(now)
        if g[v][0] == start:
            return
        dfs(g, g[v][0], start, now, score) #dを1増やして子頂点へ

    score_cand = []
    for i in range(n):
        score = []
        dfs(g, i, i, 0, score)
        score_cand.append(score)

    ans = -INF
    for i in range(n):
        cycle = score_cand[i]
        total = cycle[-1]
        if total <= 0:
            ans = max(max(cycle[:k]), ans)
        else:
            count = k // len(cycle)
            rest = k % len(cycle)

            if rest == 0:
                ans = max(count * total, (count - 1) * total + max(cycle), ans)
            else:
                ans = max(count * total + max(cycle[:rest]), (count - 1) * total + max(cycle), ans)

    print(ans)

if __name__ == '__main__':
    main()
