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
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    def dfs(G, v):
        seen[v] = True
        lis.append(v)
        for next_v in G[v]:
            if seen[next_v]:
                continue
            dfs(G, next_v)
        lis.append(v)

    n = int_input()
    g = [[] for _ in range(n)]
    for i in range(n):
        c = int_list()
        parent = c[0] - 1; count = c[1]
        if count == 0:
            continue
        for j in range(2, 2 + count):
            #print(parent, c[j] - 1)
            g[parent].append(c[j] - 1)
    #print(g)

    seen = [False] * n
    lis = []
    for v in range(n):
        if seen[v]:
            continue
        dfs(g, v)
    #print(lis)
    ans = []
    for j in range(n):
        for i in range(2 * n):
            if lis[i] == j:
                ans.append(i + 1)
    for i in range(2 * n):
        if i % 2 == 0:
            print(i // 2 + 1, ans[i], ans[i + 1])

if __name__ == '__main__':
    main()
