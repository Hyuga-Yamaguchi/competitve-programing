x, n = map(int, input().split())

if n == 0:
    print(x)
else:
    p = list(map(int, input().split()))

    p = sorted(p)
    pn = len(p)
    for i in range(pn):
        if x not in p:
            ans = x
        else:
            for j in range(100):
                if (x + j) not in p:
                    ans_1 = x + j
                    break
            for j in range(100):
                if (x - j) not in p:
                    ans_2 = x - j
                    break
            if abs(ans_1 - x) >= abs(ans_2 - x):
                ans = ans_2
            else:
                ans = ans_1
    print(ans)
