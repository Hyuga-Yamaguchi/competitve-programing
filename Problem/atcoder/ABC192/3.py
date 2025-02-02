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
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n, k = int_map()
    for i in range(k):
        n = str(n)
        lis = [None] * len(n)
        for j in range(len(n)):
            lis[j] = n[j]
        g1 = sorted(lis)
        g2 = sorted(lis, reverse = True)
        #print(g1, g2)
        g1_num = 0; g2_num = 0
        for j in range(len(n)):
            g1_num += int(g1[j]) * (10 ** j)
            g2_num += int(g2[j]) * (10 ** j)
        n = g1_num - g2_num
    print(n)

if __name__ == '__main__':
    main()
