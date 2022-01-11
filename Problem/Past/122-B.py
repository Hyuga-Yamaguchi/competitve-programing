s = input()
sn = len(s)

tmp = 0
for i in range(sn):
    for j in range(i + 1, sn + 1):
        t = s[i : j]
        tn = len(t)
        #print(t)
        cnt_t = 0
        for k in range(tn):
            if t[k] == "A" or t[k] == "G" or t[k] == "C" or t[k] == "T":
                cnt_t += 1
                #print(cnt_t)
                if cnt_t == tn and tmp < j - i:
                    tmp = j - i

print(tmp)
