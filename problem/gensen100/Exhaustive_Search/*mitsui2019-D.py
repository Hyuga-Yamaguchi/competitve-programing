n = int(input())
s = input()


ans = 0
for i in range(0, 1000):
    if 0 <= i <= 9: t = "00" + str(i)
    elif 10 <= i <= 99: t = "0" + str(i)
    elif 100 <= i <= 999: t = str(i)

"""リスト内の対象が全て探索用リストに存在するかどうか"""
"""flag = True にして、対象が探索用リストになければflag = Falseにしてbreak"""
    flag = 0
    for j in range(n):
        if t[flag] == s[j]: flag += 1
        if flag == 3: break
    if flag == 3: ans += 1
print(ans)
