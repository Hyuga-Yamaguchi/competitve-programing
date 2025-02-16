"""値が違うn個の数字が与えられます。
選び方をすべての場合について考えたとき、
それぞれの場合で選んだ数値の和を、
さらにすべて足して和を求めて下さい。
"""

list = [4, 10, 1]


def bit_plus(list):
    sum = 0
    # 0(0b000)から7(0b111)までを探索
    # range内 0b001を len(list) = 3個分ずらす→0b1000 = 8(⑽進法)
    for bit in range(1 << len(list)):
        # 0(0b000)から7(0b111)を001, 010, 100をANDで比較
        # 要素の個数0~3個までが全て一致する
        for i in range(len(list)):
            mask = 1 << i
            if bit & mask:
                sum += list[i]
    return sum


print(bit_plus(list))

###########################################
# bit全探索全列挙

n = int(input())
# xy = list(list(map(int, input().split())) for _ in range(m))

for i in range(1 << n):
    lis = []
    for j in range(n):
        if (i >> j) & 1:
            lis.append(j + 1)
    print(lis)
