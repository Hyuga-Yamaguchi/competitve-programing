import sys
sys.setrecursionlimit(10 ** 9)

n, K = map(int, input().split())
p = list(map(int, input().split()))
for i in range(n):
    p[i] -= 1
c = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(n):
    g[i].append(p[i])
    #g[p[i]].append(i)
#print(g)

def dfs(g, v):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        lis.append(next_v)
        dfs(g, next_v)
    return lis

seen = [False] * n
count = 0
cycle_lis = []
for v in range(n):
    if seen[v]:
        continue
    lis = [v]
    dfs(g, v)
    cycle_lis.append(lis)
    count += 1
#print("count =  " + str(count))
#print(cycle_lis)

INF = 10 ** 18
ans = -INF
for i in range(count):
    cycle_lis_i = cycle_lis[i] * 2; #print("cycle_lis_i = " + str(cycle_lis_i))
    l = len(cycle_lis_i); #print("l = " + str(l))
    cycle_sum = 0
    for j in range(l // 2):
        cycle_sum += c[cycle_lis_i[j]]
    #print("cycle_sum = " + str(cycle_sum))
    rest = K % (l // 2)
    if rest == 0:
        rest = l // 2
    #print("rest = " + str(rest))
    tmp_max = -INF; tmp_max_loop = -INF
    for j in range(l // 2):
        tmp = 0;
        for k in range(j, j + rest):
            tmp += c[cycle_lis_i[k]]
            #print("c = " + str(c[cycle_lis_i[k]]))
            #print("tmp = " + str(tmp))
            tmp_max = max(tmp_max, tmp)
        tmp2 = 0
        for k in range(j, j + l // 2):
            tmp2 += c[cycle_lis_i[k]]
            tmp_max_loop = max(tmp_max_loop, tmp2)
    #print("tmp_max = " + str(tmp_max))
    if cycle_sum > 0 and rest != l // 2:
        ans = max(cycle_sum * (K // (l // 2)) + tmp_max, ans)
    elif cycle_sum > 0 and rest == l // 2:
        ans = max(cycle_sum * (K // (l // 2) - 1) + tmp_max, ans)
    else:
        if K <= l // 2:
            ans = max(tmp_max, ans)
        else:
            ans = max(tmp_max_loop, ans)
print(ans)
