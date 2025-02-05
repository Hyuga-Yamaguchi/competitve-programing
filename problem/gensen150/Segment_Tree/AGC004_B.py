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


DEFAULT = INF #minの時はINFにする
QUERY = min #maxかminをえらぶ

class SegmentTree:
    def __init__(self, n):
        self.sz = 2 ** (n - 1).bit_length()
        self.dat = [DEFAULT] * self.sz * 2

    def update(self, l, r, x): #区間[l, r)の範囲で更新(0-index)
        if type(x) in [int, float]:
            x = [x] * (r - l)
        l += self.sz - 1
        r += self.sz - 1
        self.dat[l: r] = x
        while 0 < l < r:
            l = (l - 1) // 2
            r = r // 2
            for i in range(l, r):
                self.dat[i] = QUERY(self.dat[i * 2 + 1], self.dat[i * 2 + 2])

    def query(self, l, r): #区間[l, r)の範囲の最大値(最小値)を取得(0-index)
        l += self.sz - 1
        r += self.sz - 1
        res = DEFAULT
        while l < r:
            res = QUERY(res, self.dat[l])
            res = QUERY(res, self.dat[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return res

#メモリ消費を抑える時はグローバル空間に書く
def main():
    N, x = int_map()
    a = int_list()

    seg = SegmentTree(N)
    for i in range(N):
        seg.update(i, i + 1, a[i])

    ans = INF
    for k in range(N):
        cur = k * x
        for i in range(N):
            if i - k >= 0:
                cur += seg.query(i - k, i + 1)
            else:
                cur += min(seg.query(N + i - k, N), seg.query(0, i + 1))
        ans = min(ans, cur)
    print(ans)



if __name__ == '__main__':
    main()
