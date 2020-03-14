# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
"""We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000
"""

import math


def kClosest(points, K):
    def euclidean_distance(q, p):
        return math.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)

    points_w_distance = set()

    for point in points:
        distance = euclidean_distance(point, [0, 0])
        points_w_distance.add((point[0], point[1], distance))

    answer = sorted(points_w_distance, key=lambda x: x[2])[:K]

    return [list([x[0], x[1]]) for x in answer]


assert kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
