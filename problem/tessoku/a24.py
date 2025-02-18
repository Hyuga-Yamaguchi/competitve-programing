INF = 1 << 60


def int_input():
    return int(input())


def int_list(dec=False, to_tuple=False):
    result = [int(x) - dec for x in input().split()]
    return tuple(result) if to_tuple else result


def int_row(n, dec=False):
    return [int_input() - dec for _ in range(n)]


def int_row_list(n, dec=False, to_set=False):
    return (
        {int_list(dec, to_tuple=True) for _ in range(n)}
        if to_set
        else [int_list(dec) for _ in range(n)]
    )


def str_input():
    return input()


def str_list(to_tuple=False):
    result = list(input().split())
    return tuple(result) if to_tuple else result


def str_row(n):
    return [str_input() for _ in range(n)]


def str_row_list(n):
    return [str_list() for _ in range(n)]


def string_join(sep, arr):
    return sep.join(map(str, arr))


from bisect import bisect_left


def bad_lis(n, nums):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = 1
        for j in range(1, i):
            if nums[j - 1] < nums[i - 1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis(n, nums):
    dp = [0] * (n + 1)
    LEN = 0
    L = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = 1
        L[i] = min(L[i], nums[i - 1])


def main():
    n = int_input()
    nums = int_list()

    return bad_lis(n, nums)


if __name__ == "__main__":
    print(main())
