# 6. ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/

"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


def convert(s: str, numRows: int) -> str:
    answer = [""]*numRows
    asc = True
    n = 0

    while True:
        if n >= len(s):
            break

        for i in range(numRows) if asc else range(numRows-2, 0, -1):
            answer[i] = answer[i] + s[n]
            n += 1
            if n >= len(s):
                break

        asc = not(asc)

    return ''.join(answer)


assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("A", 1) == "A"
