n = int(input())

import numpy as np
import math

def magic_square(order):
    if(order % 2 == 0):
        pass
    lim = order * order
    k = 0
    tm = np.zeros(lim, dtype = int)
    m_square = tm.reshape([order, order])
    for i in range(-(order - 1) // 2, (order + 1) // 2):
        for j in range(order):
            k = k + 1
            m_square[(j - i + order) % order][(j + i + order) % order] = k
#if(check(m_square, order)):
    #print(m_square)
    m_square2 = []
    for i in range(order):
        m_square2.append((sorted(m_square[i])))
    #print(m_square2)
    return m_square2

if n <= 3:
    print("impossible")
elif n % 2 == 0: #偶数の時は可能
    print(n // 2)
    for i in range(n // 2):
        print(2, 2 * i + 1, 2 * (n - i - 1) + 1)
elif any(i ** 2 == n for i in range(2, int((10 ** 5 + 1) ** (1 / 2)))): #奇数の時は、平方数の時のみ可能
        print(int(n ** (1 / 2)))
        for j in range(int(n ** (1 / 2))):
            print(int(n ** (1 / 2)), end = " ")
            for k in range(int(n ** (1 / 2))):
                print(magic_square(int(n ** (1 / 2)))[j][k] * 2 - 1, end =" ")
            print("")
else:
    print("impossible")
