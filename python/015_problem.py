# 15. 3Sum
# https://leetcode.com/problems/3sum/

"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    res = set()

    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return list(map(list, res))


assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
assert threeSum([]) == []
assert threeSum([0, 0, 0]) == [[0, 0, 0]]
assert threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
