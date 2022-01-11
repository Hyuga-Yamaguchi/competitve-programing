n, m = map(int,input().split())
s = list(list(map(int, input().split())) for _ in range(m))
p = list(map(int,input().split()))

#print(n, m, s, p)
#print(s)
"""各スイッチのon/offパターン
0b0000000000~#0b1111111111を全部作成"""
sw2 = []
for i in range (1 << n):
    """各電球が点灯しているかどうか"""
    sw =  []
    for j in range(m):
        """各電球に関するスイッチに関するon/offパターンを全て列挙(関連しないスイッチはoff)"""
        cnt = 0
        for k in range(1, len(s[j])):
            if i >> (s[j][k] - 1) & 1 == 1:
                cnt += 1
            else:
                cnt += 0
            #print(bin(i), j, k, cnt)
        sw.append(cnt)
        #print(sw)
    sw2.append(sw)
#print(sw2)

ans2 = 0
for j in range(len(sw2)):
    ans = 0
    for k in range(len(sw2[j])):
        if sw2[j][k] % 2 == p[k]:
            ans += 1
    if ans == len(sw2[j]):
        ans2 += 1

print(ans2)
#     sw_cnd = []
#     for j in range(len[sw]):
#         for k in range(m):
#             if  sw[j][k] % 2 == p[j]:
#                 i_bin = bin(i)
#                 sw_cnd.append(i_bin)
#
# sw = set(sw)
# print(sw)
# print(len(sw))
