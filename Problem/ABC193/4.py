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
float_INF = float('inf')
INF = 1 << 60
MOD = 10 ** 9 + 7

def main():
    k = int_input()
    s = str_input()
    t = str_input()
    def point(str):
        u = [0] * 10
        for i in range(5):
            u[int(str[i])] += 1
        point = 0
        for i in range(10):
            point += i * (10 ** u[i])
        return point

    #高橋くんが勝つ場合のカードリスト
    win_card = []
    for i in range(1, 10):
        for j in range(1, 10):
            s = s[0:4] + str(i)
            t = t[0:4] + str(j)
            #print(s, t)
            if point(s) > point(t):
                win_card.append([i, j])
    #print(win_card)

    #カードの残り枚数
    u = [k] * 10
    for i in range(4):
        u[int(s[i])] -= 1
        u[int(t[i])] -= 1
    #print(u)

    ans = 0
    for i in win_card:
        s_rev = u[i[0]]
        t_rev = u[i[1]]
        #print(i)
        if i[0] == i[1]:
            if s_rev >= 2:
                ans += Decimal(str((s_rev / (9 * k - 8)) * ((t_rev - 1)) / (9 * k - 9)))
                #print("flag1")
            else:
                ans += 0
                #print("flag2")
        else:
            if s_rev >= 1 and t_rev >= 1:
                ans += Decimal(str((s_rev / (9 * k - 8)) * (t_rev / (9 * k - 9))))
                #print("flag3")
            else:
                ans += 0
                #print("flag4")
    print(ans)





if __name__ == '__main__':
    main()
