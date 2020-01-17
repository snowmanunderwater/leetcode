# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

"""Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

# Runtime: 24 ms, faster than 87.77% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.


def generate(numRows):
    if numRows == 0:
        return []

    answer = []
    temp = []
    answer.append([1])

    for i in range(1, numRows):
        temp.append(1)

        if i > 1:
            for r in range(i-1):
                temp.insert(i, answer[-1][r] + answer[-1][r+1])

        temp.append(1)
        answer.append(temp.copy())
        temp.clear()
    
    return answer


assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert generate(0) == []
