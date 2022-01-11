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
    n, q = int_map()
    mat = int_row_list(n)

    for i in range(q):
        a, b = int_map()
        cur_mat = []
        for (r, h) in mat:
            if r >= a and h <= b:
                cur_mat.append((r, h))
        cur_mat.sort(key = itemgetter(1), reverse = True)
        cur_mat.sort(key = itemgetter(0))
        #print(cur_mat)

        a = [None] * len(cur_mat)
        for i in range(len(cur_mat)):
            a[i] = cur_mat[i][1]

        seq = []
        for a_i in a:
            pos = bisect_left(seq, a_i)
            if len(seq) <= pos:
                seq.append(a_i)
            else:
                seq[pos] = a_i
        print(cur_mat, len(seq))
        if len(cur_mat) == 0:
            print(0)
        else:
            print(len(cur_mat) - len(seq) + 1)

if __name__ == '__main__':
    main()
