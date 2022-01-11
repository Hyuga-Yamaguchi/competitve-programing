import operator

n = int(input())
ab = list(list(map(int, input().split())) for _ in range(n))

ab = sorted(ab, key = operator.itemgetter(1))

#print(ab)

cur_end_time = 0
flag = True
for i in range(n):
    cur_end_time += ab[i][0]
    if cur_end_time <= ab[i][1]:
        flag = True
        #print(cur_end_time)
    else:
        flag = False
        #print(cur_end_time)
        print("No")
        exit(0)
print("Yes")
