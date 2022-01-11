n = int(input())
INF = 10 ** 9

ans = INF
for a in range(1, n):
    b = n - a
    na, nb = a, b
    cnt = 0
    for i in range(6):
        cnt += na % 10
        cnt += nb % 10
        na //= 10
        nb //= 10
    #print("cnt = " + str(cnt))
    if ans >= cnt:
        ans = cnt
        #print(ans)
print(ans)
