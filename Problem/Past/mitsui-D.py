#TLE

n = int(input())
s = input()
sn = len(s)

v_lis = []
for i in range(1000):
    if i >= 100:
        v = str(i)
    elif 10 <= i <= 99:
        v = "0" + str(i)
    elif 0 <= i <= 9:
        v = "00" + str(i)
    #print(v)
    tmp_1, tmp_2, tmp_3 = sn + 1, sn + 1, sn + 1
    for j in range(sn):
        if s[j] == v[0] and tmp_1 >= j:
            tmp_1 = j
    if tmp_1 <= sn:
        #print(tmp_1, v)
        for k in range(tmp_1 + 1, sn):
            if s[k] == v[1] and tmp_2 >= k:
                tmp_2 = k
    if tmp_2 <= sn:
            #print(tmp_2, v)
        for l in range(tmp_2 + 1, sn):
            if s[l] == v[2] and tmp_3 >= l:
                tmp_3 = l
                if tmp_3 <= sn:
                    #print(tmp_3, v)
                    v_lis.append(v)

print(len(v_lis))
