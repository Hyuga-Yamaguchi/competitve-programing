n = int(input())
a = list(map(int, input().split()))

def gcd(x, y):
    # 大きい方を被除数、小さい方を除数とする
    dividend = max(x, y)
    divider = min(x, y)

    if divider == 0:
        return dividend

    # 最大公約数を見つけるまで繰り返す
    while dividend % divider != 0:
        # 除算を行い、その除数を次回の被除数、剰余を次回の除数として処理を繰り返す
        r = dividend % divider
        dividend = divider
        divider = r

    # 一方がもう一方を割り切れた時点で、その除数を最大公約数とみなせる
    return divider


for i in range(n - 1):
    a[i + 1] = gcd(a[i], a[i + 1])
print(a[-1])
