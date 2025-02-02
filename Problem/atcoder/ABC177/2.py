s = input()
t = input()

ls = len(s)
lt = len(t)

cnt = []
for i in range(ls - lt + 1):
    cnt1 = 0
    for k in range(lt):
        if t[k] == s[i: i + lt][k]:
            cnt1 += 1
            cnt.append(cnt1)
            #print(t[i:k], s[i:], k-i)
        else:
            cnt.append(0)
            #print(t[i:k], k - i)
#print(cnt)
print(lt - max(cnt))
