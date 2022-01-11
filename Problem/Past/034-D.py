n,k=map(int,input().split())

x=[list(map(int,input().split())) for i in range(n)]
print(x)

#それぞれの容器で含有食塩量を出す
salt=[x[i][0]*x[i][1]*0.01 for i in range(n)]
print(salt)

#1.ok=0.0, ng=101.0 として、ok と ng の間隔が十分小さくなるまで以下を繰り返す
#   1.okとngの中間にある値 x について、以下の方法でC(x) が成立するか判定する
#       1.(𝑤𝑖𝑝𝑖–𝑤𝑖𝑥)/100 の値で降順にソートする
#       2.上位K個の合計が 0 以上ならC(x)成立。そうでないなら不成立となる
#   2.C(x) が成立したならば、ok = mid と更新する。不成立ならば ng = mid と更新する
#2.ok の値が答え
