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
flaot_INF = float('inf')
INF = 1 << 60
MOD = 10 ** 9 + 7

def main():
    h, w, a, b = int_map()
    used = [[False] * w for _ in range(h)] #現在位置が(i, j)で、すでに敷き詰められたマスがused = True
    def rec(i, j, a):
        #最後まで探索して、長方形のタイルを使い切っているなら、組み合わせを+1して終了する
        if i == h:
            return a == 0
        #列の端まで行ったら次の行へ行く
        if j == w:
            return rec(i + 1, 0, a)

        #すでに置かれているのなら次のマスへ
        if used[i][j]:
            return rec(i, j + 1, a)

        res = 0

        #縦置き
        if i + 1 < h and not used[i + 1][j] and a > 0:
            used[i][j] = used[i + 1][j] = True
            res += rec(i, j + 1, a - 1)
            used[i][j] = used[i + 1][j] = False #初期化

        #横置き
        if j + 1 < w and not used[i][j + 1] and a > 0:
            used[i][j] = used[i][j + 1] = True
            res += rec(i, j + 1, a - 1)
            used[i][j] = used[i][j + 1] = False #初期化

        #正方形をおく
        res += rec(i, j + 1, a)

        return res
    print(rec(0, 0, a))

if __name__ == '__main__':
    main()
