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


ans = INF
#メモリ消費を抑える時はグローバル空間に書く
def main():
    def candidate(str0, str1, str2):
        lis0 = []; lis1 = []; lis2 = []
        for i in range(2 * n):
            if lis[i][1] == str0:
                lis0.append(lis[i][0])
            elif lis[i][1] == str1:
                lis1.append(lis[i][0])
            elif lis[i][1] == str2:
                lis2.append(lis[i][0])
        return [lis0, lis1, lis2]

    n = int_input()
    lis = [None] * (2 * n)
    r = 0; g = 0; b = 0
    for i in range(2 * n):
        a, c = str_map()
        lis[i] = (int(a), c)
        if c == "R":
            r += 1
        elif c == "G":
            g += 1
        elif c == "B":
            b += 1

    if r % 2 == 0 and g % 2 == 0 and b % 2 == 0:
        print(0)
        exit()
    elif r % 2 == 0:
        [A, B, C]  = candidate("G", "B", "R")
    elif g % 2 == 0:
        [A, B, C]  = candidate("R", "B", "G")
    elif b % 2 == 0:
        [A, B, C]  = candidate("G", "R", "B")

    A.sort(); B.sort(); C.sort()#Cが偶数

    ans = INF
    for x in A:
        index = bisect_left(B, x)
        #print(x, index)
        if index == len(B):
            ans = min(ans, abs(B[index - 1] - x))
        elif index == 0:
            ans = min(ans, abs(B[0] - x))
        else:
            ans = min(ans, abs(B[index] - x), abs(B[index - 1] - x))

    if len(C) > 0:
        cur_a = INF
        for x in A:
            index = bisect_left(C, x)
            #print(x, index)
            if index == len(C):
                cur_a = min(cur_a, abs(C[index - 1] - x))
            elif index == 0:
                cur_a = min(cur_a, abs(C[0] - x))
            else:
                cur_a = min(cur_a, abs(C[index] - x), abs(C[index - 1] - x))

        cur_b = INF
        for x in B:
            index = bisect_left(C, x)
            #print(x, index)
            if index == len(C):
                cur_b = min(cur_b, abs(C[index - 1] - x))
            elif index == 0:
                cur_b = min(cur_b, abs(C[0] - x))
            else:
                cur_b = min(cur_b, abs(C[index] - x), abs(C[index - 1] - x))

        ans = min(ans, cur_a + cur_b)

    print(ans)

if __name__ == '__main__':
    main()
