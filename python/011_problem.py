# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

"""Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

# Runtime: 128 ms, faster than 79.26% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.7 MB, less than 7.37% of Python3 online submissions for Container With Most Water.


def maxArea(height):
    length = len(height)
    ind1 = 0
    ind2 = length - 1
    val1 = val2 = 0
    max_vol = 0

    while True:

        vol = min(height[ind1], height[ind2]) * (ind2 - ind1)
        if vol > max_vol:
            max_vol = vol

        if abs(ind1 - ind2) < 2:
            break

        if height[ind1] > height[ind2]:
            ind2 -= 1
        elif height[ind1] < height[ind2]:
            ind1 += 1
        elif height[ind1] == height[ind2]:
            if height[ind1+1] > height[ind2-1]:
                ind1 += 1
            elif height[ind1+1] < height[ind2-1]:
                ind2 -= 1
            elif height[ind1+1] == height[ind2-1]:
                ind1 += 1
        
    return max_vol


assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea([2,3,4,5,18,17,6]) == 17
assert maxArea([1,1]) == 1
assert maxArea([1,2,1]) == 2
