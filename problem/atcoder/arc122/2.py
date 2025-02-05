import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
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

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    a = int_list()

    def f(x):
        sigma = 0
        for i in range(n):
            sigma += (a[i] - min(a[i], 2 * x))
        return n * x + sigma

    low = 0; high = INF
    while high - low > 10 ** (-7):
        c1 = (low * 2 + high) / 3
        c2 = (low + high * 2) / 3
        if f(c1) > f(c2):
            low = c1
        else:
            high = c2
        #print(pos, left, right)
    #print(low, high)
    print(f(high) / n)

if __name__ == '__main__':
    main()
