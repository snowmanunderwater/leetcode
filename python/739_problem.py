# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

"""Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 
"""


def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)
    return ans


assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures([55,38,53,81,61,93,97,32,43,78]) == [3,1,1,2,1,1,0,1,1,0]
assert dailyTemperatures([34,80,80,34,34,80,80,80,80,34]) == [1,0,0,2,1,0,0,0,0,0]
assert dailyTemperatures([34,80,80,80,34,80,80,80,34,34]) == [1,0,0,0,1,0,0,0,0,0]
