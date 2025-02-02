import operator

n = int(input())
st = list(list(map(int, input().split())) for _ in range(n))

#リストの任意の位置の値にしたがってソート
st1 = sorted(st, key = operator.itemgetter(1))
st2 = sorted(st, key = operator.itemgetter(0))

#print(st)

#貪欲に選ぶ
res = 0
current_end_time = 0
for i in range(n):
    #最後に選んだ区間とかぶるものは除く
    #print("current_end_time = " + str(current_end_time))
    if st1[i][0] < current_end_time:
        continue
    res += 1
    current_end_time = st1[i][1]
print(res)

#貪欲に選ぶ
res_ = 0
current_start_time = 0
for i in range(n):
    #最後に選んだ区間とかぶるものは除く
    #print("current_end_time = " + str(current_end_time))
    if st2[i][0] < current_start_time:
        continue
    res_ += 1
    current_start_time = st2[i][0]
print(res_)
