import numpy as np
import math

n = int(input())

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
    print(m_square2)


# def check(m_square, order):
#     ok = (math.pow(order, 3) + order) // 2
#     t1 = t2 = t3 = t4 = 0
#     for i in range(order):
#         t1 += m_square[i][i]
#         t2 += m_square[i][order - 1 - i]
#     t3 = np.sum(m_square, axis=0)
#     t4 = np.sum(m_square, axis=1)
#     if(t1 != ok):
#         return False
#     if(t2 != ok):
#         return False
#     for x in t3:
#         if(x != ok):
#             return False
#     for y in t4:
#         if(y != ok):
#             return False
#     return True

magic_square(n)
