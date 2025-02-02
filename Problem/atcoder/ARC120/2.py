import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
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
    h, w = int_map()
    S = [None] * h
    for i in range(h):
        S[i] = str_input()
    #print(S)

    ans = 1; flag = True
    for i in range(h + w - 1):
        blue = 0; red = 0; dot = 0
        cnt = 0
        for j in range(h):
            k = i - j
            if k < 0 or k >= w:
                continue
            if S[j][k] == "R":
                red += 1
            elif S[j][k] == "B":
                blue += 1
            else:
                dot += 1
        #print("blue, red", blue, red)
        if blue >= 1 and red >= 1:
            flag = False
            print(0)
            exit()
        elif blue >= 1 and red == 0:
            cnt += 1
        elif blue == 0 and red >= 1:
            cnt += 1
        elif blue == 0 and red == 0:
            cnt += 2
        #print("i, cnt", i, cnt)
        ans *= (cnt % mod)
    print(ans % mod)


if __name__ == '__main__':
    main()
