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
flaot_INF = float('inf')
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main():
    def prime_eratostheness(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, n + 1):
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return list(i for i in range(n + 1) if is_prime[i])
    y = prime_eratostheness(50)
    #print(y)

    n = int_input()
    x = int_list()

    ans = INF
    for bit in range(1 << len(y)):
        tmp = 1
        for i in range(len(y)):
            if (bit >> i) & 1:
                tmp *= y[i]
        # if ans >= tmp:
        #     continue
        flag = True
        for i in x:
            if gcd(tmp, i) == 1:
                flag = False
        if flag:
            ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()
