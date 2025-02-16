from typing import List
from bisect import bisect_left, bisect_right


def self_bisect_left(arr: List[int], target: int):
    """
    arr に対して target を二分探索して、左側の挿入点を返す。
    arr の中に target がある場合、その index を返す。
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def self_bisect_right(arr: List[int], target: int):
    """
    arr に対して target を二分探索して、右側の挿入点を返す。
    arr の中に target がある場合、その index に increment したものを返す。
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left


test_input = [
    {"arr": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67], "target": 44},
    {"arr": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67], "target": 47},
    {"arr": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67], "target": 11},
    {"arr": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67], "target": 67},
    {"arr": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67], "target": 9},
    {"arr": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67], "target": 70},
]

for ti in test_input:
    arr = ti["arr"]
    target = ti["target"]

    print("Input:", ti)
    print("\tself_bisect_left:", self_bisect_left(arr, target))
    print("\tbisect.bisect_left:", bisect_left(arr, target))
    print("\tself_bisect_right:", self_bisect_right(arr, target))
    print("\tbisect.bisect_right:", bisect_right(arr, target))
    print("")
