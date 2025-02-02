n = int(input())
dist = list(list(map(int, input().split())) for _ in range(n))
print(dist)

INF = 100

#ハミルトン閉路の最小コスト
dp = [[INF] * (n + 1) for _ in range((1 << n) + 1)]
dp[0][0] = 0

for S in range(1 << n): #S:= {0, 1,..., n - 1}の部分集合
    for v in range(n): #v:= 各点　ただし、部分集合(S)に追加する要素(当然、探索するときはSには含まれない)
        for u in range(n): #u:=各点　ただし、部分集合(S)の最後の要素(当然、探索するときはSに含まれる)
            if S != 0 and not (S & (1 << u)):
                continue
                # 部分集合Sについて、Sが空集合ではなく、
                #最後の要素をuで探索し、それを含まない場合は、何もしない
            if (S & (1 << v)) == 0:
                #部分集合Sに対して、それを含んでいない要素vを決める
                #u->始点,v->終点となる
                if v != u:
                    #u->vに経路がある場合は、それを探索するとコストが最大化するので、探索しない
                    #部分集合Sにvを追加したものので、Sの最終要素がvのものは、
                    #現時点の値と(部分集合Sで始点uの値+u->vのコスト)の最小値をとる
                    dp[S | (1 << v)][v] = min(dp[S | (1 << v)][v], dp[S][u] + dist[u][v])
            print(dp)

if dp[(1 << n) - 1][0] != INF:
    print(dp[(1 << n) - 1][0])
else:
    print(-1)
