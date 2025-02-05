def int_input():
    return int(input())


def int_list():
    return list(map(int, input().split()))


def int_row(N):
    return [int_input() for _ in range(N)]


def int_row_list(N):
    return [int_list() for _ in range(N)]


def str_input():
    return input()


def str_list():
    return list(input().split())


def str_row(N):
    return [str_input() for _ in range(N)]


def str_row_list(N):
    return [str_list() for _ in range(N)]


def bit_search(arr):
    n = len(arr)
    return [[arr[j] for j in range(n) if i >> j & 1] for i in range(1 << n)]


INF = 1 << 60


def main():
    n, m = int_list()
    switches = [list(map(lambda s: s - 1, switche[1:])) for switche in int_row_list(m)]
    ps = int_list()

    cnt = 0
    for l in bit_search(range(n)):
        l_set = l
        if all(
            sum(1 for s in switche if s in l_set) % 2 == ps[idx]
            for idx, switche in enumerate(switches)
        ):
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(main())
