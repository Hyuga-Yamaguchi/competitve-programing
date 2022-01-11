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
a, b, k = int_map()
na = copy(a)

def pos_b(a, b):
    global k
    lis = [None] * (a + 1)
    lis[0] = 1
    for i in range(1, a + 1):
        lis[i] = lis[i - 1] * (b + i - 1) // i
    #print("lis", lis)

    sum_lis = [None] * (a + 1)
    sum_lis[0] = 1
    for i in range(1, a + 1):
        sum_lis[i] = sum_lis[i - 1] + lis[i]
    #print(sum_lis)

    b_pos = a - bisect_left(sum_lis, k)
    #print("b_pos", b_pos)

    k -= sum_lis[bisect_left(sum_lis, k) - 1]
    #print("k", k)

    return b_pos

b_lis = []
for i in range(b, 0, -1):
    #print("a, b, i", a, b, i)
    rest = pos_b(a, i)
    b_lis.append(rest)
    a -= rest
#print("b_lis",b_lis)

index = [None] * b
index[0] = b_lis[0]
for i in range(1, len(b_lis)):
    index[i] = index[i - 1] + 1 + b_lis[i]
#print(index)

index = set(index)
ans = ""
for i in range(na + b):
    if i in index:
        ans += "b"
    elif not i in index:
        ans += "a"
print(ans)
