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
    lis = [None] * n
    for i in range(n):
        t, l, r = int_map()
        if t == 1:
            lis[i] = [l, r]
        elif t == 2:
            lis[i] = [l, r - 0.1]
        elif t == 3:
            lis[i] = [l + 0.1, r]
        elif t == 4:
            lis[i] = [l + 0.1, r - 0.1]

    ans = 0
    for i in range(n - 1):
        a = lis[i][0]; b = lis[i][1]
        for j in range(i + 1, n):
            c = lis[j][0]; d = lis[j][1]
            if a <= c <= b <= d:
                ans += 1
            elif c <= a <= d <= b:
                ans += 1
            elif c <= a <= b <= d:
                ans += 1
            elif a <= c <= d <= b:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
