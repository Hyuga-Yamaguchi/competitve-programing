t1 = 0.1
t2 = 0.2
t3 = 0.3

#float型での計算
if t1 + t2 == t3:
    print("True")
else:
    print("False")
"""
Flase
"""

#許容絶対誤差を10 ** (-9)　として計算
epsilon = 10 ** (-9)

if t3 - epsilon <= t1 + t2 <= t3 + epsilon:
    print("True")
else:
    print("False")
"""
True
"""
