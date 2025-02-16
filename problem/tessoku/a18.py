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


def subset_sum_dp(n, s, nums):
    """
    Determines whether a subset sum of s can be formed.

    Parameters:
        n (int): Length of the array
        s (int): Target sum
        nums (List[int]): List of given integers

    Returns:
        bool: True if a subset sum of s can be formed, otherwise False
    """
    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(s + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            if j - nums[i - 1] >= 0 and dp[i - 1][j - nums[i - 1]]:
                dp[i][j] = True
    return dp[n][s]


def main():
    n, s = int_list()
    nums = int_list()

    return "Yes" if subset_sum_dp(n, s, nums) else "No"


if __name__ == "__main__":
    print(main())
