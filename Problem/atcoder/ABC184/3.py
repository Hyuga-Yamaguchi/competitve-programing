r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r = r1 - r2
c = c1 - c2

#移動0
#startとgoalが同じ点
if (r, c) == (0, 0):
    print(0)
#移動1
#斜め上にある時
elif r == c or r == -c:
    print(1)
#３マス以内にある時
elif abs(r) + abs(c) <= 3:
    print(1)
#移動２
#斜め上にはないパリティ
elif (r + c) % 2 == 0:
    print(2)
#6マス以内にある時
elif abs(r) + abs(c) <= 6:
    print(2)
#斜めに移動+３マス以内移動
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    print(2)
#移動３
else:
    print(3)
