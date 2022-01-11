n = int(input())
a = list(map(int, input().split()))

rby = [1, 0, 0]
cnt = 3
MOD = 10 ** 9 + 7
if a[0] != 0:
    print(0)
    exit()
for i in range(1, n):
    if a[i] in rby:
        cnt *= rby.count(a[i])
        index_rby = rby.index(a[i])
        rby[index_rby] += 1
    else:
        print(0)
        exit()
    #print("cnt = " + str(cnt))
    #print(rby)
print(cnt % MOD)
