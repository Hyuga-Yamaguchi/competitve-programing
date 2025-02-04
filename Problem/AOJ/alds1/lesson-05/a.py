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


INF = 1 << 60


def bit_search(arr):
    n = len(arr)
    return [[arr[j] for j in range(n) if i >> j & 1] for i in range(1 << n)]


def main():
    n = int_input()
    a = int_list()
    q = int_input()
    ms = int_list()

    bit_a = bit_search(a)

    return "\n".join(["yes" if m in set(map(sum, bit_a)) else "no" for m in ms])


if __name__ == "__main__":
    print(main())
