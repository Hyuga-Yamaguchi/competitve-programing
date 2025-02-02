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
    sub_s = str_input()
    s = [None] * (2 * n)
    for i in range(2 * n):
        s[i] = sub_s[i]
    q = int_input()
    #print(s)
    flag = False
    for i in range(q):
        t, a, b = int_map()
        a -= 1; b -= 1
        if t == 1:
            if flag:
                a = (a + n) % (2 * n); b = (b + n) % (2 * n)
            s[a], s[b] = s[b], s[a]
        else:
            flag = not flag
    #print(flag)
    if flag:
        s = s[n:2 * n] + s[0:n]
    print("".join(s))

if __name__ == '__main__':
    main()
