import math
#import numpy as np
import sys
import collections
import itertools
import operator
import bisect
import heapq
import random
sys.setrecursionlimit(10 ** 9)
MOD=10**9+7
INF=float("inf")

n,m=map(int,input().split())
a=list(map(int,input().split()))
yakusuu=set()

def prime_factorize(x):
    while x % 2 == 0:
        yakusuu.add(2)
        x //= 2
    f = 3
    while f * f <= x:
        if x % f == 0:
            yakusuu.add(f)
            x //= f
        else:
            f += 2
    if x != 1:
        yakusuu.add(x)
    return a
for i in range(n):
    prime_factorize(a[i])
#print(yakusuu)
yakusuu = list(yakusuu)
len_yakusuu = len(yakusuu)
cnt_lis = set()
M = [True] * m
for i in range(m):
    for j in range(len_yakusuu):
        if M[]
        if max((i + 1), yakusuu[j]) % min((i + 1), yakusuu[j])==0:
            M[i] = False

print(M)
print(len(cnt_lis))
cnt_lis=list(cnt_lis)
cnt_lis.sort()
for i in range(len(cnt_lis)):
    print(cnt_lis[i])
