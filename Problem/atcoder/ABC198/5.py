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
def str_input(): return input()
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
flag = True

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    c = int_list()
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = int_map()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    print(g)

    def dfs(g, v, p = -1):
        print("on the way(v)", v)
        if cnt[c[v]] == 0:
            good[v] = True
        cnt[c[v]] += 1
        print("cnt(go)", cnt)
        print("good", good)

        for t in g[v]:
            if t == p:
                continue #探索が親方向へ逆流するのを防ぐ
            #print("on the way(c)", c)

            #cはvの各子頂点を動く。この時,cの親はvとなる
            dfs(g, t, v)
            #print("on the way back(c)", c)
        print("on the way back(v)", v)
        cnt[c[v]] -= 1
        print("cnt(back)", cnt)

    cnt = [0] * 10
    good = [False] * n
    dfs(g, 0)

    #print(good)

    for i in range(n):
        if good[i]:
            print(i + 1)

if __name__ == '__main__':
    main()
