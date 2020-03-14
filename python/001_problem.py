# 1. Two Sum
# https://leetcode.com/problems/two-sum/
"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Runtime: 44 ms, faster than 92.38% of Python3 online submissions for Two Sum.
# Memory Usage: 14.2 MB, less than 54.18% of Python3 online submissions for Two Sum.


def twoSum(nums, target):
    second_el = {}
    for i, num in enumerate(nums):
        if num in second_el:
            first = second_el[num]
            second = i
            return [first, second]
        second_el[target - num] = i


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([2, 7, 11, 15], 13) == [0, 2]
assert twoSum([2, 7, 11, 15], 26) == [2, 3]
