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
    q = int_input()
    bag = [] #ふくろ
    heapify(bag)
    rec = [] #記録
    cumsum = [0] * q #後で足す用
    cur = 0
    cnt = 0 #取り出したボールの数

    for i in range(q):
        query = str_input()
        if len(query) >= 3:
            t = int(query[0])
            num = int(query[2:])
        else:
            t = int(query[0])
        if t == 1:
            heappush(bag, num - cur)
        elif t == 2:
            cumsum[cnt] += num
            cur += num
        else:
            b = heappop(bag)
            rec.append(b)
            cnt += 1
    print("bag", bag)
    print("rec", rec)
    print("cumsum", cumsum)
    print("cur", cur)

    cumsum_ = [None] * q
    cumsum_[0] = cumsum[0]
    for i in range(1, q):
        cumsum_[i] = cumsum_[i - 1] + cumsum[i]
    print("cumsum_", cumsum_)


    for i in range(len(rec)):
        print(rec[i] + cumsum_[i])

if __name__ == '__main__':
    main()

'''sample
10
1 3 bag = [3] kiroku = []
1 5 bag = [3, 5] kiroku = []
3 bag = [5] kiroku = [3]
1 4 bag = [4, 5] kiroku = [3]
2 2
1 6 bag = [4, 4, 5] kiroku = [3]
2 5
1 7 bag = [0, 4, 4, 5] kiroku = [3]
3 bag = [4, 4, 5] kiroku = [3 ,0]
3 bag = [4, 5] kiroku = [3, 0, 4] -> [3, 7, 11](最後に2のqueryの累積和を足す)
'''
