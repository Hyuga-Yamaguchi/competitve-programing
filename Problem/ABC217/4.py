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
def str_row_list(N): return [list(str_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

class BinaryTrie:
    def __init__(self, max_query = 2 * (10 ** 5), bitlen = 30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    # xの挿入
    def insert(self, x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x >> i & 1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1

    # 昇順x番目の値
    def kth_elm(self, x):
        pt, ans = 0, 0
        for i in range(self.bitlen-1, -1, -1):
            ans <<= 1
            if self.nodes[2 * pt] != -1 and self.cnt[self.nodes[2 * pt]] > 0:
                if self.cnt[self.nodes[2 * pt]] >= x:
                    pt = self.nodes[2 * pt]
                else:
                    x -= self.cnt[self.nodes[2 * pt]]
                    pt = self.nodes[2 * pt + 1]
                    ans += 1
            else:
                pt = self.nodes[2 * pt + 1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か
    def lower_bound(self, x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1, -1, -1):
            if pt == -1: break
            if x >> i & 1 and self.nodes[2 * pt] != -1:
                ans += self.cnt[self.nodes[2 * pt]]
            pt = self.nodes[2 * pt + (x >> i & 1)]
        return ans

#メモリ消費を抑える時はグローバル空間に書く
def main():
    l, q = int_map()
    bt = BinaryTrie()
    bt.insert(0)
    bt.insert(l)

    for i in range(q):
        c, x = int_map()
        if c == 1:
            bt.insert(x)
        else:
            p = bt.lower_bound(x)
            print(bt.kth_elm(p) - bt.kth_elm(p - 1))

if __name__ == '__main__':
    main()
