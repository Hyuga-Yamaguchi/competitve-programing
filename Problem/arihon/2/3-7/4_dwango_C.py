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

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, m = int_map()
    a = int_list()
    b = int_list()

    N = max(sum(a), sum(b))
    K = max(len(a), len(b))

    def count(arr, length):
        kosu = []
        cur = arr[0]; cnt = 1
        for i in range(1, length):
            if cur != arr[i]:
                kosu.append(cnt)
                cur = arr[i]
                cnt = 1
            else:
                cnt += 1
            if i == length - 1:
                kosu.append(cnt)
        return kosu


    #分割数を求める
    p = [[0] * (K + 1) for _ in range(N + 1)]
    for j in range(1, K + 1):
        p[0][j] = 1

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if i >= j:
                p[i][j] = p[i][j - 1] + p[i - j][j]
            else:
                p[i][j] = p[i][i]
    print(p)

    kosu_a = count(a, n); kosu_b = count(b, m)
    print(kosu_a, kosu_b)

    set_a = len(kosu_a); set_b = len(kosu_b)





if __name__ == '__main__':
    main()
