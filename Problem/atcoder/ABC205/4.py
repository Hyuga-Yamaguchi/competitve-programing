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
INF = 1 << 100
MOD = 10 ** 9 + 7
mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, q = int_map()
    a = int_list()

    #対象の区間
    start = 0;
    b = []
    for i in range(n):
        if start == a[i]:
            start = a[i] + 1
            continue
        b.append([start, a[i] - 1])
        start = a[i] + 1
    b.append([a[-1] + 1, INF])

    #0->1に修正,aに1が含まれている場合は消去
    if b[0][1] == 0:
        b = b[1:]
    else:
        b[0][0] = 1
    #print(b)

    #c:それぞれの区間の個数
    c = [None] * len(b)
    for i in range(len(b)):
        c[i] = b[i][1] - b[i][0] + 1
    #print(c)

    #cの累積和
    cumsum_c = [None] * len(b)
    cumsum_c[0] = c[0]
    for i in range(1, len(b)):
        cumsum_c[i] = cumsum_c[i - 1] + c[i]
    cumsum_c = [0] + cumsum_c
    #print(cumsum_c)

    for i in range(q):
        k = int_input()
        index = bisect_left(cumsum_c, k)
        num = k - cumsum_c[index - 1]
        ans = b[index - 1][0] + num - 1
        print(ans)

if __name__ == '__main__':
    main()
