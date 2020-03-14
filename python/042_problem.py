# https://leetcode.com/problems/trapping-rain-water/


def calc(arr, base):
    # print('From calc', arr, base)
    return len([x for x in arr if x <= base])


# one way solution
def rain_water(height):
    l = 0
    r = len(height) - 1
    l_rec, r_rec = 0, 0
    already = 0
    answer = 0

    while l < len(height) and r >= 0 and l != r:
        # print('coord:', (l, r), 'val:', (height[l], height[r]), 'record:', (l_rec, r_rec))

        if height[l] > l_rec:
            if height[l] > 0 and height[r] > 0:
                if already != min(height[l], height[r]):
                    answer += calc(height[l:r+1], already)
                already = min(height[l], height[r])
            l_rec = height[l]

        if height[r] > r_rec:
            if height[l] > 0 and height[r] > 0:
                if already != min(height[l], height[r]):
                    answer += calc(height[l:r+1], already)
                already = min(height[l], height[r])
            r_rec = height[r]

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return answer


# |            |
# |       #    |
# |   #~~~##~# |
# | #~##~######|
# +------------+

# |            |
# |       #    |
# |   #~~~##~# |
# | #~##~######|
# +------------+

assert rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert rain_water([0,3,0,2,1,0,1,3,2,1,2,1]) == 12
assert rain_water([0,3,0,2,1,0,1,2,2,1,2,1]) == 7
assert rain_water([0, 1, 0, 1]) == 1
assert rain_water([2, 0, 2]) == 2
assert rain_water([2, 0, 1, 2]) == 3
assert rain_water([30, 0, 30]) == 30

