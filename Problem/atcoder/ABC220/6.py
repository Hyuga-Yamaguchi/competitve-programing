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
    n = int_input()
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        u, v = int_map()
        u -= 1; v -= 1
        g[u].append(v)
        g[v].append(u)
    #print(g)

    def dfs(g, v, p = -1, d = 0):
        depth[v] = d
        for c in g[v]:
            if c == p:
                continue #探索が親方向へ逆流するのを防ぐ
            dfs(g, c, v, d + 1) #dを1増やして子頂点へ

        #帰りがけ時に、部分木のサイズを求める
        subtree_size[v] = 1 #自分自身
        for c in g[v]:
            if c == p:
                continue
            #子頂点を根とする部分木のサイズを加算する
            subtree_size[v] += subtree_size[c]

    depth = [None] * n
    subtree_size = [None] * n
    dfs(g, 0)
    #print(depth, subtree_size)

    def cnt(g, v, p=-1, s=sum(depth)):
        ans[v] = s
        for c in g[v]:
            if c == p:
                continue
            ns = s + (n - subtree_size[c]) - subtree_size[c]
            ans[c] = ns
            cnt(g, c, v, ns)

    ans = [None] * n
    cnt(g, 0)

    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()
