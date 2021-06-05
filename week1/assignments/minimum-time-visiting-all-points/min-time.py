#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
'''
intuition: 
dont care about diagonals. take the max of (horizontal, vertical) moves for each pair of points
'''
class Solution:
    def minTimeToVisitAllPoints(self, points): # one-liner
        # return sum(max(abs(a[0] - b[0]), abs(a[1] - b[1]))for a, b in zip(points, points[1:]))
        return sum(max(abs(x-y) for x, y in zip(a, b)) for a, b in zip(points, points[1:]))

    def minTimeToVisitAllPoints2(self, points):
        res = 0
        for p1, p2 in zip(points, points[1:]):
            res += max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))
        return res
# @lc code=end

points = [[3,2],[-2,2]]
points = [[1,1],[3,4],[-1,0]]
ans = Solution().minTimeToVisitAllPoints(points)
print(ans)