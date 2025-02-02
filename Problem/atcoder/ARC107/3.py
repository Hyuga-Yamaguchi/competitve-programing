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
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        #各要素の親要素番号を格納するリスト　要素が根の場合は、-(そのグループの要素数)

    """要素xが属するグループの根を返す"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    """要素xが属するグループと要素yが属するグループとを併合する"""
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    """要素xが属するグループのサイズ（要素数）を返す"""
    def size(self, x):
        return -self.parents[self.find(x)]

    """要素x, yが同じグループに属するかどうかを返す"""
    def same(self, x, y):
        return self.find(x) == self.find(y)

    """要素xが属するグループに属する要素をリストで返す"""
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    """すべての根の要素をリストで返す"""
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    """グループの数を返す"""
    def group_count(self):
        return len(self.roots())

    """{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す"""
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    """print()での表示用"""
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, K = int_map()
    a = int_row_list(n)

    uf_row = UnionFind(n)
    uf_col = UnionFind(n)

    #列の入れ替え
    for j in range(n):
        for k in range(j + 1, n):
            flag_row = True; flag_col = True
            for i in range(n):
                if a[i][j] + a[i][k] > K:
                    flag_row = False
                if a[j][i] + a[k][i] > K:
                    flag_col = False
            if flag_row:
                uf_row.union(j, k)
            if flag_col:
                uf_col.union(j, k)
    #print(uf_row.all_group_members())
    #print(uf_col.all_group_members())

    d_row = uf_row.all_group_members()
    d_col = uf_col.all_group_members()

    row = 1
    for key in d_row:
        row *= factorial(len(d_row[key])) % mod
    col = 1
    for key in d_col:
        col *= factorial(len(d_col[key])) % mod
    print((row * col) % mod)

if __name__ == '__main__':
    main()
