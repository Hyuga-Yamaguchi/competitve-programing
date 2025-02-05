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
    n, k = int_map()
    arr = []
    for i in range(n):
        a, b = int_map()
        arr.append([a, b])

    arr.sort()
    #print(arr)
    pos = 0; money = k; flag = True
    for i in range(n):
        a = arr[i][0]; b = arr[i][1]
        if pos + money >= a:
            money = money - (a - pos) + b; pos = a
            #print("1", pos, money)
        else:
            pos += money
            #print("2", pos, money)
            flag = False
            break
    if flag:
        print(pos + money)
    else:
        print(pos)


if __name__ == '__main__':
    main()
