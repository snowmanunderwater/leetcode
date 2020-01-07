# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

"""There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

# Runtime: 92 ms, faster than 84.05% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.


def findMedianSortedArrays(nums1, nums2):
    temp = sorted(nums1 + nums2)
    lenth = len(temp)
    if lenth % 2 == 0:
        return (temp[lenth // 2 - 1] + temp[lenth // 2]) / 2
    else:
        return temp[lenth // 2]


assert findMedianSortedArrays([1, 3], [2]) == 2.0 
assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
