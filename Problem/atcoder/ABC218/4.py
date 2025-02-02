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
def int_tuple(): return tuple(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
def int_row_tuple(N): return [int_tuple() for _ in range(N)]
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
    xy = int_row_tuple(n)
    xy_hash = set()
    for i in range(n):
        xy_hash.add(xy[i])

    xy.sort(key = itemgetter(1))
    xy.sort(key = itemgetter(0))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            (x0, y0) = xy[i]; (x1, y1) = xy[j]
            #print(x0, y0, x1, y1)
            if x0 >= x1 or y0 >= y1:
                continue
            p1 = (x1, y0); p2 = (x0, y1)
            #print("p1",p1, "p2", p2)
            if p1 in xy_hash and p2 in xy_hash:
                #print("flag")
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
