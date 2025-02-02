import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque, defaultdict
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
flaot_INF = float('inf')
INF = 1 << 60
MOD = 10 ** 9 + 7

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

def main():
    n = int_input()
    a = int_list()

    a_gcd = 0
    for i in range(n):
        if i == 0:
            a_gcd = a[0]
        else:
            a_gcd = gcd(a_gcd, a[i])
    if a_gcd != 1:
        print("not coprime")
        exit()

    u = [0] * (10 ** 6 + 1)
    flag = True
    D = prime_factor_table(max(a))
    for i in range(n):
        dic = prime_factor(a[i], D)
        for p in dic.keys():
            if p != 1 and u[p] >= 1:
                flag = False
            u[p] += 1
    if flag:
        print("pairwise coprime")
    else:
        print("setwise coprime")

if __name__ == '__main__':
    main()
