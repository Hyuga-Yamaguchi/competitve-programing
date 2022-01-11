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
#flag = True

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, m = int_map()
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = int_map()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    def dfs(g, v, pos, p = -1):
        global flag
        seen[v] = True
        print("on the way", v, flag)
        print("seen(go)", seen)
        print("finished(go)", finished)
        for c in g[v]:
            #逆流を防ぐ
            print("c", c)
            if c == p:
                print("c == p")
                continue
            #完全終了した頂点はスルー
            if finished[c]:
                print("finished[c]")
                continue
            #サイクル検出
            #print("seen[c]", seen[c])
            #print("finished[c]", finished[c])
            if seen[c] and not finished[c]:
                print("flag_false")
                flag = False
                pos = c
                return
            dfs(g, c, pos, v)

            print("pos", pos)
            if pos != -1:
                print("pos != -1")
                return

        finished[v] = True
        print("on the way back", v, flag)
        print("seen(come)", seen)
        print("finished(come)", finished)

    ans = 0
    seen = [False] * n
    finished = [False] * n
    for v in range(n):
        if seen[v]:
            continue
        flag = True
        pos = -1
        dfs(g, v, pos)
        print("flag", flag)
        if flag:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
