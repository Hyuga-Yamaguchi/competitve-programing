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

#メモリ消費を抑える時はグローバル空間に書く
def main():
    s = str_input()
    o_set = set(); hatena_o_set = set()
    for i in range(len(s)):
        if s[i] == "o":
            o_set.add(i)
            hatena_o_set.add(i)
        if s[i] =="?":
             hatena_o_set.add(i)
    #print(o_set, hatena_o_set)

    t = ""; cnt = 0
    for i in range(10000):
        if 0 <= i <= 9:
            t = "000" + str(i)
        elif 10 <= i <= 99:
            t = "00" + str(i)
        elif 100 <= i <= 999:
            t = "0" + str(i)
        else:
            t = str(i)
        t_set = set()
        for j in range(4):
            t_set.add(int(t[j]))
        if o_set <= t_set and t_set <= hatena_o_set:
            #print(t)
            cnt += 1
    print(cnt)




if __name__ == '__main__':
    main()
