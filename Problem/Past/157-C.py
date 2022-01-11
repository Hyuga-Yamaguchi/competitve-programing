n, m = map(int, input().split())
s = list(list(map(int, input().split())) for _ in range(m))

# def get_unique_list(seq):
#     seen = []
#     return [x for x in seq if x not in seen and not seen.append(x)]
#
# s = get_unique_list(s)
# #print(s)
# x = 0
# for i in range(len(s)):
#     if s[i] == [1, 0] and n >= 1:
#         print(-1)
#         exit()
#     for j in range(i + 1, len(s)):
#         if s[i][0] == s[j][0] and s[i][1] != s[j][1]:
#             #print(s[i], n)
#             print(-1)
#             exit()
#         else:
#             break
#     for k in range(1, n + 1):
#         if s[i][0] == k:
#             x += s[i][1] * (10 ** (n - k))
#             #print(k, x, i)
# print(x)

#0~10**nまでの数字を探索　条件に合致するかどうか判定

print(s)
lis = []
for i in range(10 ** n):
    i = str(i)
    for j in range(m):
        if s[j][1] == i[s[j][0]]:
            i = int(i)
            lis.append(i)
        else:
            break

if lis == []:
    print(-1)
else:
    print(min(lis))
