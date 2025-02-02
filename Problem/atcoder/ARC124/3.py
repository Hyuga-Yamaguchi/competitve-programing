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

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    a = [None] * n; b = [None] * n
    for i in range(n):
        A, B = int_map()
        a[i] = A; b[i] = B
    #XとYはそれぞれa[0]とb[0]の約数
    x = make_divisors(a[0])
    y = make_divisors(b[0])
    #print(x, y)

    ans = 0
    for x_num in x:
        for y_num in y:
            flag = True
            for i in range(n):
                if not (a[i] % x_num == 0 and b[i] % y_num == 0) and not (a[i] % y_num == 0 and b[i] % x_num == 0):
                    flag = False
            if flag:
                ans = max(ans, lcm(x_num, y_num))
    print(ans)


if __name__ == '__main__':
    main()
