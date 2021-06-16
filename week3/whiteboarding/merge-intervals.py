#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for a, b in sorted(intervals, key=lambda x: x[0]):
            if not res or res[-1][-1] < a:
                res.append([a, b])
            elif res[-1][-1] >= a and res[-1][-1] < b:
                res[-1][-1] = b
        return res
# @lc code=end

Sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[1,4],[2,3]]
ans = Sol.merge(intervals)
print(ans)