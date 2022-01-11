import operator

n = int(input())
ab = list(list(map(int, input().split())) for _ in range(n))
cd = list(list(map(int, input().split())) for _ in range(n))

ab = sorted(ab, key = operator.itemgetter(1))[::-1]
cd = sorted(cd)

INF = 10 ** 8
#print(ab, cd)

ans = 0
for i in range(n):
     for j in range(n):
         if cd[i][0] > ab[j][0] and cd[i][1] > ab[j][1]:
             #print("cd[i] = " + str(cd[i]), "ab[j] = " + str(ab[j]))
             ans += 1
             ab[j] = [INF, INF]
             cd[i] = [-INF, -INF]
             #print("ab = " + str(ab))
print(ans)
