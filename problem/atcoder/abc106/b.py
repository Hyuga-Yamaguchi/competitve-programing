def int_input():
    return int(input())


def int_list():
    return list(map(int, input().split()))


def int_row(N):
    return [int_input() for _ in range(N)]


def int_row_list(N):
    return [int_list() for _ in range(N)]


def str_input():
    return input()[:-1]


def str_list():
    return list(input().split())


def str_row(N):
    return [str_input() for _ in range(N)]


def str_row_list(N):
    return [str_list() for _ in range(N)]


def main():
    n = int_input()

    cnt = 0
    for i in range(1, n + 1, 2):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div == 8:
            cnt += 1

    return cnt


if __name__ == "__main__":
    print(main())
