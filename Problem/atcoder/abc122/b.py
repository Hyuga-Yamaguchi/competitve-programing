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


def main():
    s = str_input()

    max_len = 0
    cur_len = 0

    for char in s:
        if char in "ATGC":
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 0

    return max_len


if __name__ == "__main__":
    print(main())
