import itertools

n ,k = map(int, input().split())
t = list(list(map(int, input().split())) for _ in range(n))

ans = 0
for i in itertools.permutations(range(2, n + 1)):
    lis = list(i); lis.insert(0, 1); lis.append(1)
    #print(lis)

    time = 0
    for i in range(n):
        start, goal = lis[i] - 1, lis[i + 1] - 1
        time += t[start][goal]
    if time == k:
        ans += 1
print(ans)
