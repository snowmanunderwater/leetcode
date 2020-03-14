# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
"""A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:

Your solution should be in logarithmic complexity.
"""

# Runtime: 40 ms, faster than 91.41% of Python3 online submissions for Find Peak Element.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.


def findPeakElement(nums):
    length = len(nums)
    if length < 2:
        return 0
    if length == 2:
        return nums.index(max(nums))
    for n in range(1, length - 1):
        if nums[n - 1] < nums[n] > nums[n + 1]:
            return n

    return nums.index(max(nums))


assert findPeakElement([1, 2, 3, 1]) == 2
assert findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 1 or 5
