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
    s_ = int_list()
    t_ = int_list()

    s = [None] * n
    t = [None] * n; min_t = INF; idx_t = 0
    for i in range(n):
        s[i] = [s_[i], i]
        t[i] = [t_[i], i]
        if min_t >= t_[i]:
            min_t = t_[i]
            idx_t = i
    #print(s, t, idx_t)

    s = s[idx_t:n] + s[0:idx_t]
    t = t[idx_t:n] + t[0:idx_t]
    #print(s, t)

    cur = 0
    ans = []
    for i in range(n):
        if i == 0:
            ans.append((t[i][0], t[i][1]))
            cur = t[i][0]
        else:
            if cur + s[i - 1][0] <= t[i][0]:
                ans.append((cur + s[i - 1][0], t[i][1]))
                cur += s[i - 1][0]
            else:
                ans.append((t[i][0], t[i][1]))
                cur = t[i][0]
    #print(ans)

    ans.sort(key = itemgetter(1))
    for i in range(n):
        print(ans[i][0])



if __name__ == '__main__':
    main()
