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
INF = 1 << 80
MOD = 10 ** 9 + 7
mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int(input())
    a = int_list()

    def OR_keisan(arr):
        lis_or = arr[0]
        for j in range(1, len(arr)):
            lis_or = lis_or | arr[j]
        return lis_or

    ans = INF
    for bit in range(1 << (n - 1)):
        lis = [0] * (n - 1)
        for i in range(n - 1):
            if (bit >> i) & 1:
                lis[i] = 1
        lis.append(1)
        #print("lis =", lis)
        index_0 = 0; index_1 = n
        bun_lis = []
        for i in range(n):
            if lis[i] == 1:
                index_1 = i + 1
            if lis[i] == 0:
                continue
            #print(index_0, index_1)
            b = a[index_0:index_1]
            if b:
                bun_lis.append(b)
            index_0 = index_1
        #print("bun_lis", bun_lis)

        or_lis = []
        for i in bun_lis:
            arr_or = OR_keisan(i)
            or_lis.append(arr_or)
        #print(or_lis)

        xor = or_lis[0]
        for i in range(1, len(or_lis)):
            xor = xor ^ or_lis[i]
        ans = min(ans, xor)
    print(ans)






    # a_xor = INF
    # for i in range(1, n):
    #     a1 = a[:i]
    #     a2 = a[i:]
    #     a1_or = a1[0]; a2_or = a2[0]
    #     for j in range(1, len(a1)):
    #         a1_or = a1_or | a1[j]
    #     for j in range(1, len(a2)):
    #         a2_or = a2_or | a2[j]
    #     a_xor = min(a_xor, a1_or ^ a2_or)
    # print(a_xor)

if __name__ == '__main__':
    main()
