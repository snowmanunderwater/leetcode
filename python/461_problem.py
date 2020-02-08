# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

"""The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""

# Runtime: 28 ms, faster than 64.83% of Python3 online submissions for Hamming Distance.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Hamming Distance.


def hammingDistance(x: int, y: int) -> int:
    raznica = 0

    new_x = "{0:b}".format(x)
    new_y = "{0:b}".format(y)
    
    length = len(max(new_x, new_y, key=lambda x: len(x)))
    
    new_x = new_x.zfill(length)
    new_y = new_y.zfill(length)

    for i in range(length):
        raznica += abs(int(new_x[i]) - int(new_y[i]))
    
    return raznica


assert hammingDistance(1, 4) == 2
assert hammingDistance(1, 5) == 1
assert hammingDistance(3, 5) == 2
assert hammingDistance(1577962638, 1727613287) == 16
