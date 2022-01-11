import matplotlib.pyplot as plt
import numpy as np

print("How long distance carry the chain in one stroke?")
"""１回に送るA面移動量"""
distance = int(input())

"""Dtb端から中間受入センサまでの距離"""
l1 = 18910
"""中間受入から中間C/0後退限アタッチメントまでの距離"""
l2 = 7200
"""Dtbのデッドライン"""
Dtb_Deadline = 3000

"""挿入する鋼板の幅リスト"""
W = []
for i in range(10):
    W.append(4500)

dp = [[-1] * len(W) for _ in range(2 * len(W) + 1)]
dp[0][0] = W[0] // 2

"""搬送可否のflag"""
flag = 0
for i in range(2 * len(W)):
    """rest:中間受入センサ蹴った後の送り量"""
    rest = 0
    """シミュレーション"""
    for j in range(len(W)):
        if W[j] // 2 <= dp[i][j] < l1:
            dp[i + 1][j] = dp[i][j] + distance
            if dp[i + 1][j] >= l1:
                rest = l1 + l2 - dp[i + 1][j]
                dp[i + 1][j] = l1 + l2

    for j in range(len(W)):
        if 0 <= dp[i + 1][j] < l1:
            dp[i + 1][j] += rest

    """dp更新"""
    if 0 <= i < len(W) - 1:
        dp[i + 1][i + 1] = W[i + 1] // 2
    for j in range(len(W)):
        if l1 <= dp[i + 1][j] < l1 + l2:
            print("Error = The sensor is kicked twice.")
            flag = 1
        elif 0 <= dp[i + 1][j] < W[j] + Dtb_Deadline:
            print("Error = The plates is remained in DTb.")
            flag = 2
if flag == 0:
    print("OK")

#print(dp)
cnt = 0
for i in range(len(dp)):
    tmp = 0
    for j in range(len(dp[i])):
        if 0 <= dp[i][j] < l1:
            tmp += 1
        if l1 - 500 <= dp[i][j] < l1:
            print("Warning = The risk of kicked sensor twice is remained.")
            flag = 3
    cnt = max(cnt, tmp)
print(cnt - 1)

"""グラフの描写"""
buffer = 500
fig = plt.figure(figsize = (6, 4))
ax = fig.add_subplot(111)
ax.axhline(l1, ls = "--", color = "red")
plt.text(0, l1 + 500, "Chukan-Ukeire sensor = " + str(l1), color = "red")
ax.axhline(l1 - buffer, ls = "--", color = "blue")
plt.text(0, l1 - 1800, "Chukan-Ukeire sensor buffer = " + str(l1 - buffer), color = "blue")
ax.axhline(Dtb_Deadline, ls = "--", color = "red")
plt.text(0, Dtb_Deadline + 500, "Dtb_Deadline = " + str(Dtb_Deadline), color = "red")

for i in range(len(dp)):
    for j in range(len(dp[i])):
        color_list = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf']
        if dp[i][j] >= 0:
            plt.scatter(i, dp[i][j], c = color_list[j % len(color_list)])
        if set(W) == 1:
            plt.title("A-area Transport Simulation (W = " + str(W[0]) + "mm, d = " + str(distance) + "mm)")
        else:
            plt.title("A-area Transport Simulation (W = random, d = " + str(distance) + "mm)")
        if flag == 0:
            fig.text(0.02, 0.95, "OK", color = "blue", fontsize = 12)
        elif flag == 1:
            fig.text(0.02, 0.95, "Error = The sensor is kicked twice.", color = "red", fontsize = 12)
        elif flag == 2:
            fig.text(0.02, 0.95, "Error = The plates is remained in DTb.", color = "red", fontsize = 12)
        elif flag == 3:
            fig.text(0.02, 0.95, "Warning = The risk of kicked sensor twice is remained.", color = "orange", fontsize = 12)
        fig.text(0.8, 0.95, "max " + str(cnt - 1) + "plates", color = "cyan", fontsize = 12)
        plt.xlabel("Plate Number")
        plt.ylabel("Position")
        plt.grid(True)
#plt.plot(x1, y1)
plt.show()
