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
    while True:
        [x, y] = int_list()

        if [x, y] == [0, 0]:
            break

        cnt = 0
        for i in range(1, x + 1):
            for j in range(i + 1, x + 1):
                for k in range(j + 1, x + 1):
                    if i + j + k == y:
                        cnt += 1

        print(cnt)


if __name__ == "__main__":
    main()
