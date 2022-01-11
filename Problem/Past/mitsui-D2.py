n = int(input())
s = input()

ans = []
#0００から９９９の数列を生成
for i in range(10):
    for j in range(10):
        for k in range(10):
            v = str(i) + str(j) + str(k)
            #Si = V1となるようなiの中で最も小さいiを探す。
            for l in range(n):
                if s[l] == v[0]:
                    ans_0 = v[0]
                    p1 = l
                    print(v, ans_0, p1)
                else:
                    break
            #print(p1)
#             for m in range(p1 + 1, n):
#                 if v[1] == s[m]:
#                     ans_1 = v[1]
#                     p2 = m
#                     break
#                 else:
#                     break
#             for o in range(p2 + 1, len(s)):
#                 if v[2] == s[o]:
#                     ans_2 = v[2]
#                     p3 = o
#                     break
#                 else:
#                     break
# ans.appemd(ans_O + ans1 + ans2)
#
# print(len(ans))
