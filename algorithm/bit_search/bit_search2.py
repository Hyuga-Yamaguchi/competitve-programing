"""bit全探索
N個の正の整数a=[a0,a1,a2,,,,,an-1]と正の整数について、
aの中から何個かの整数を選んで総和をWとすることができるかの判定
"""

n = int(input())
a = list(map(int, input().split()))
w = int(input())

exist = False
for bit in range(1 << n):
    sum = 0
    for i in range(n):
        if bit & (1 << i):
            sum += a[i]
            print(bit, i)
    if sum == w:
        exist = True

if exist:
    print("Yes")
else:
    print("No")
