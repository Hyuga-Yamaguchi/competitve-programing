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
    n, k = int_map()
    t = str(n)

    ans = 0
    #n以下で0が含まれるもの
    cnt_0 = 0
    #桁数-1までの0の数
    for i in range(len(t)):
        if i <= 1:
            continue
        else:
            cnt_0 += 9 * (10 ** (i - 1) - 9 ** (i - 1))
    #桁数の0を含む数
    cnt_0_sub = 1
    for i in range(len(t)):
        if i == 0:
            cnt_0_sub *= int(t[i])
        else:
            cnt_0_sub *= int(t[i]) + 1
    cnt_0 += cnt_0_sub
    print(cnt_0)

    #桁数の積が1,2,3,5,7のもの
    #桁数-1のもの
    if k < 2:
        cnt_p = len(t) - 1
        if n > int("1" * len(t)):
            cnt_p += 1
    elif k < 3:
        cnt_p = len(t) - 1 + len(t) * (len(t) - 1) // 2
        if n < int("1" * len(t)):
            cnt_p += 0
        elif n < int("2" + "1" * (len(t) - 1)):
            cnt_p += 1
        else:
            cnt_p += 2
    elif k < 5:
        cnt_p = len(t) - 1 + 2 * len(t) * (len(t) - 1) // 2
        if n < int("1" * len(t)):
            cnt_p += 0
        elif n < int("2" + "1" * (len(t) - 1)):
            cnt_p += 1
        elif n < int("3" + "1" * (len(t) - 1)):
            cnt_p += 2
        else:
            cnt_p += 3
    elif k < 7:
        cnt_p = len(t) - 1 + 3 * len(t) * (len(t) - 1) // 2
        if n < int("1" * len(t)):
            cnt_p += 0
        elif n < int("2" + "1" * (len(t) - 1)):
            cnt_p += 1
        elif n < int("3" + "1" * (len(t) - 1)):
            cnt_p += 2
        elif n < int("5" + "1" * (len(t) - 1)):
            cnt_p += 3
        else:
            cnt_p += 4
    else:
        cnt_p = len(t) - 1 + 4 * len(t) * (len(t) - 1) // 2
        if n < int("1" * len(t)):
            cnt_p += 0
        elif n < int("2" + "1" * (len(t) - 1)):
            cnt_p += 1
        elif n < int("3" + "1" * (len(t) - 1)):
            cnt_p += 2
        elif n < int("5" + "1" * (len(t) - 1)):
            cnt_p += 3
        elif n < int("7" + "1" * (len(t) - 1)):
            cnt_p += 4
        else:
            cnt_p += 5
    print(cnt_p)

    #合成数
    def prime_eratostheness(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, n + 1):
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return set(i for i in range(n + 1) if is_prime[i])

if __name__ == '__main__':
    main()
