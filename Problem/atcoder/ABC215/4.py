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
    n, m = int_map()
    a = int_list()

    def prime_factor_table(n): #最大の素因数
        table = [0] * (n + 1)

        for i in range(2, n + 1):
            if table[i] == 0:
                for j in range(i + i, n + 1, i):
                    table[j] = i
        return table

    def prime_factor(n, prime_factor_table): #素因数分解
        prime_count = defaultdict(int)

        while prime_factor_table[n] != 0:
            prime_count[prime_factor_table[n]] += 1
            n //= prime_factor_table[n]
        prime_count[n] += 1

        return prime_count

    max_lis = prime_factor_table(10 ** 5 + 1)

    div = set() #n(loga ** 2)
    for i in range(n):
        d = prime_factor(a[i], max_lis)
        #print(d)
        for key in d:
            div.add(key)
    #print(div)

    b = []
    for i in range(1, m + 1):
        d = prime_factor(i, max_lis)
        b.append(d)
    #print(b)

    ans = []
    for i in range(len(b)):
        dic = b[i]
        flag = True
        for key in dic:
            if key in div:
                flag = False
        if flag:
            ans.append(i + 1)

    if not 1 in ans:
        print(len(ans) + 1)
        print(1)
    else:
        print(len(ans))
    for ans_ in ans:
        print(ans_)

if __name__ == '__main__':
    main()
