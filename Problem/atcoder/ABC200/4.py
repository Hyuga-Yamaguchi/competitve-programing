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
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    a = int_list()

    cnt = min(n, 8)
    u = [[] for _ in range(200)]
    for i in range(1, 1 << cnt):
        sig = 0
        s = []
        for j in range(cnt):
            if (i & 1 << j):
                s.append(j + 1)
        for j in s:
            sig += a[j - 1]
        sig %= 200
        u[sig].append(s)

    for i in u:
        if len(i) >= 2:
            print("Yes")
            print(len(i[0]), end = " ")
            print(* i[0])
            print(len(i[1]), end = " ")
            print(* i[1])
            exit()
    print("No")



if __name__ == '__main__':
    main()
