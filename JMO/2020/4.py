for i in range(1, 10 ** 4):
    a = str(i ** 2)
    b = str(i ** 3)
    if len(a) + len(b) == 8:
        lis = []
        for j in range(len(a)):
            lis.append(a[j])
        for j in range(len(b)):
            lis.append(b[j])
        cnt = 0
        for j in range(1, 9):
            if lis.count(str(j)) != 1:
                break
            else:
                cnt += 1
        if cnt == 8:
            ans = i
            print(ans)
