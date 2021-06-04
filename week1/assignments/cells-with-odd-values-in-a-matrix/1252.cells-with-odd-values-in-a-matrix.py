#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
from typing import List
class Solution:
    '''
    intuition:
    1. no need to construct a whole empty matrix. 
    2. declare two arrays to hold the indices of rows/columns. 
    3. iterate over the indices, and increment rows[i] cols[j] accordingly. 
    4. we dont care about the sum value, traverse the rows/cols - if the sum is odd, add it to result
    '''
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        return sum((x + y) % 2 for y in cols for x in rows)
# @lc code=end

m = 2
n = 3
indices = [[0,1],[1,1]]

# m = 2
# n = 2
# indices = [[1,1],[0,0]]
Sol = Solution()
ans = Sol.oddCells(m, n, indices)
print(ans)