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
    n, m = int_map()
    tube = [None] * m
    for i in range(m):
        k = int_input()
        a = deque(int_list())
        tube[i] = a

    cnt = [[] for _ in range(n + 1)]
    que = deque()

    for i in range(m):
        top = tube[i][0]
        cnt[top].append(i)

    for i in range(n + 1):
        if len(cnt[i]) == 2:
            que.append(i)

    while que:
        now = que.popleft()
        for p in cnt[now]:
            tube[p].popleft()
            if tube[p]:
                cnt[tube[p][0]].append(p)
                if len(cnt[tube[p][0]]) == 2:
                    que.append(tube[p][0])

    for a_ in tube:
        if a_:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()
