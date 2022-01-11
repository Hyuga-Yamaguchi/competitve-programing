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

n=int(input())
graph=[[] for _ in range(n)]
for i in range(n):
    temp=list(map(int,input().split()))
    temp=temp[2:]
    for j in range(len(temp)):
        temp[j]-=1
        graph[i].append(temp[j])
#print(graph)
for i in range(n):
    graph[i].sort()

seen=[False] *n
time_in=[0]*n
time_out=[0]*n

time = 0
def dfs(x):
    global time
    print("before_seen", id(seen))
    seen[x]=True
    print("after_seen", id(seen))
    time_in[x]=time
    print("before_time", id(time))
    time += 1
    print("after_time", id(time))
#    if len(graph[x])==0:
#        time_out[x]=time
#        return
#    else:
    for v in graph[x]:
        if seen[v]:
            continue
        #print("go_x, v, time",x, v, time)
        dfs(v)
        #print("back_x, v, time", x, v, time)
        time_out[v]=time
        time += 1
        #print("time_in", time_in)
        #print("time_out", time_out)
        time_out[x] = time

for i in range(n):
    if seen[i]:
        continue
    time += 1
    dfs(i)
#print(time_in)
#print(time_out)

for i in range(n):
    print(i + 1, time_in[i], time_out[i])
