"""引数がimmutableの場合"""
def func(n1, n2):
    print("n1_before", id(n1))
    print("n2_before", id(n2))
    n1 = n1 + 4
    n2 = n2 - 3
    print("n1_after", id(n1))
    print("n2_after", id(n2))
    return n1, n2

x = 10; y = 20
print("x_before", id(x))
print("y_before", id(y))
print("func(x, y) = " + str(func(x, y)))
print("x, y = " + str(x) + ", " + str(y))
print("x_after", id(x))
print("y_after", id(y))
"""出力結果
x_before 4543735168
y_before 4543735488
n1_before 4543735168
n2_before 4543735488
n1_after 4543735296
n2_after 4543735392
func(x, y) = (14, 17)
x, y = 10, 20
x_after 4543735168
y_after 4543735488
"""
"""
①実引数(x, y)を仮引数(n1, n2)に渡す時は参照渡し
②n1 = n1 + 4, n2 = n2 - 3の時、数値型はimmutableなので、n1, n2は新たなIDに再定義される
③結果(x, y)と(n1, n2)について値渡しのような挙動となる
"""

"""引数がmutableの場合"""
def func2(n):
    print("n_before", id(n))
    n[0] = 7
    print("n_after", id(n))
    return n

z = [10, 20]
print("z_before", id(z))
print("func2(z) = " + str(func2(z)))
print("z = " + str(z))
print("z_after", id(z))
"""
z_before 4328374752
n_before 4328374752
n_after 4328374752
func2(z) = [7, 20]
z = [7, 20]
z_after 4328374752
"""
"""
①実引数zを仮引数nに渡す時は参照渡し
②n[0] = 7の時、list型はmutableなので、nは同じIDに上書きされる
③結果zとnについて参照渡しのような挙動となる
"""
