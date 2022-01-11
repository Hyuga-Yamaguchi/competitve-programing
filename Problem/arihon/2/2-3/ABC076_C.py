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
    t = str_input()
    ls = len(s); lt = len(t)

    lis = []
    for i in range(ls - lt + 1):
        sub_s = s[i:lt + i]
        flag = True
        for j in range(lt):
            if sub_s[j] != "?" and sub_s[j] != t[j]:
                flag = False
        if flag:
            cand_sub = s[:i] + t + s[lt + i:]
            cand = ""
            for k in range(ls):
                if cand_sub[k] == "?":
                    cand += "a"
                else:
                    cand += cand_sub[k]
            lis.append(cand)
    #print(lis)

    if not lis:
        print("UNRESTORABLE")
        exit()
    lis.sort()
    print(lis[0])

if __name__ == '__main__':
    main()
