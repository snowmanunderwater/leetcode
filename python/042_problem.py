# https://leetcode.com/problems/trapping-rain-water/


def rain_water(height):
    l = 0
    r = len(height) - 1
    l_max, r_max = 0, 0
    answer = 0

    while l < r:
        if height[l] > l_max:
            l_max = height[l]
        elif height[l] < l_max:
            answer += l_max - height[l]

        if height[r] > r_max:
            r_max = height[r]
        elif height[r] < r_max:
            answer += r_max - height[r]

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return answer


assert rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert rain_water([0, 3, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 12
assert rain_water([0, 3, 0, 2, 1, 0, 1, 2, 2, 1, 2, 1]) == 7
assert rain_water([0, 1, 0, 1]) == 1
assert rain_water([2, 0, 2]) == 2
assert rain_water([2, 0, 1, 2]) == 3
assert rain_water([30, 0, 30]) == 30
