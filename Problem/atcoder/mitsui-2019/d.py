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
    n = int_input()
    s = str_input()

    secrets = [f"{i:03d}" for i in range(1000)]
    count = 0

    for secret in secrets:
        idx = 0
        for char in s:
            if idx == 3:
                break
            if secret[idx] == char:
                idx += 1
        if idx == 3:
            count += 1

    return count


if __name__ == "__main__":
    print(main())
