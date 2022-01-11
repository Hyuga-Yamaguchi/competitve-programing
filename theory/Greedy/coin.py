"""
貪欲法＝あと先のことを考えずに「その場での最善」を選択することを繰り返す方法論。

500円玉、100円玉、50円玉、5円玉、１円玉がそれぞれ、a[0]~a[5]枚ある。
これらを用いてX円支払うとき、使用するコインの枚数の最小値はいくらか。
"""

value = [500, 100, 50, 10, 5, 1]
a = list(map(int, input().split()))

x = int(input())

result = 0
for i in range(6):
    #枚数制限がない場合の枚数
    add = x // value[i]
    #枚数制限を考慮
    if add > a[i]:
        add = a[i]
    #残りの金額を求めて、答えに枚数を加算する
    x -= value[i] * add
    result += add

print(result)
