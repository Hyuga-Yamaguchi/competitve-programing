cnt = 0
for i in range(0, 10):
    for j in range(0, 10):
        s = "2" + str(i) + "2" + str(j)
        if int(s) % 7 == 0:
            cnt += 1
print(cnt)
