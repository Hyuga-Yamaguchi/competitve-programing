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
def str_input(): return input()
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
    s1 = input()
    s2 = input()
    s3 = input()

    str_lis = set()
    for i in range(len(s1)):
        str_lis.add(s1[i])
    for i in range(len(s2)):
        str_lis.add(s2[i])
    for i in range(len(s3)):
        str_lis.add(s3[i])
    str_lis = tuple(str_lis)
    #print(str_lis)

    if len(str_lis) >= 11:
        print("UNSOLVABLE")
    else:
        numlis = [str(x) for x in range(10)]
        for v in permutations(numlis, len(str_lis)):
            mydict = {}
            for i in range(len(str_lis)):
                mydict[str_lis[i]] = v[i]
            #print(mydict)
            t1 = ""; t2 = ""; t3 = ""
            for i in range(len(s1)):
                t1 += mydict[s1[i]]
            for i in range(len(s2)):
                t2 += mydict[s2[i]]
            for i in range(len(s3)):
                t3 += mydict[s3[i]]
            if t1[0] == "0" or t2[0] == "0" or t3[0] == "0":
                continue
            if int(t3) == int(t1) + int(t2):
                print(int(t1))
                print(int(t2))
                print(int(t3))
                exit()
        print("UNSOLVABLE")

if __name__ == '__main__':
    main()
