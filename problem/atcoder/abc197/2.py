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
def str_input(): return input().split()
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
    h, w , x, y = int_map()
    S = [None] * h
    for i in range(h):
        S[i] = input()[:-1]
    #print(S)

    cnt_h = 0; cnt_w = 0
    for i in range(w):
        if y - 1 <= i < w:
            #print(S[y - 1][i])
            if S[x - 1][i] == ".":
                cnt_w += 1
            else:
                break
    for i in range(y - 2, -1, -1):
        if S[x - 1][i] == ".":
            cnt_w += 1
        else:
            break
    #print(cnt_w)

    for i in range(h):
        if x - 1 <= i < h:
            if S[i][y - 1] == ".":
                cnt_h += 1
            else:
                break
    for i in range(x - 2, -1, -1):
        if S[i][y - 1] == ".":
            cnt_h += 1
        else:
            break
    #print(cnt_h)
    print(cnt_w + cnt_h - 1)



if __name__ == '__main__':
    main()
