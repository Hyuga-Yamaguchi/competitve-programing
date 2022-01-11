n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    print(0)
else:

    ans = 1
    i = 0
    while (i <= n - 1):
        if ans <= 10 ** 18:
            ans *= a[i]
            i += 1
        else:
            break

    #print(i)
    if ans <= 10 ** 18:
        print(ans)
    else:
        print(-1)
