import bisect

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

left = 0; right = a[-1] * b[-1]
while right - left > 1:
    mid = left + (right - left) // 2

    cnt = 0
    for i in range(n):
        iter = bisect.bisect_right(b, mid // a[i])
        cnt += iter
    if cnt >= k:
        right = mid
    else:
        left = mid
print(right)
