N = int(input())

def cnt(x, y):
    return y - x + 1

for i in range(1, 7):
    if 10 ** (i - 1) <= N < 10 ** i:
        dig = i
        # print(dig)
        if dig == 1:
            print(cnt(1, N))
        elif dig == 2:
            print(cnt(1, 9))
        elif dig == 3:
            print(cnt(1, N) - cnt(10, 99))
        elif dig == 4:
            print(cnt(1, N) - cnt(10, 99) - cnt(1000, N))
        elif dig == 5:
            print(cnt(1, N) - cnt(10, 99) - cnt(1000, 9999))
        elif dig == 6:
            print(cnt(1, N) - cnt(10,99) - cnt(1000,9999) - cnt(100000, N))
