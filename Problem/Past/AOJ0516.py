while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input()))

    for i in range(1, n):
        a[i] = a[i - 1] + a[i]
    #print(a)

    ans = 0
    for i in range(n - k):
        ans = max(a[i + k] - a[i], ans)
        #print(ans)
    print(ans)
# """""""""""""""""""""""""""""""""""""""""""""""""

# while True:
#     n, k = [int(i) for i in input().split()]
#     if n == 0 and k == 0:
#         break
#     a = [int(input()) for i in range(n)]
#     s = sum(a[0:k])
#     max = s
#     for i in range(k, n):
#         s = s + a[i] - a[i - k]
#         if s > max:
#             max = s
#     print(max)
