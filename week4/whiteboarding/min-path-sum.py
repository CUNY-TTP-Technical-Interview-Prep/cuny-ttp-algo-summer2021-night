#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid):
        # improvement: save space by modifying the original grid
        if not grid: return
        m, n = map(len, (grid, grid[0]))
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    def minPathSum2(self, grid):
        '''
        intuition: dynamic programming. create a dynamic 2-d array where dp[i][j] represents the min sum from the upper left cell to the current cell. first initialize dp with its first row and first column. then for each subsequent cell, we can find the min sum by grid[i][j] + min(dp[i-1][j], dp[i][j-1]), taking the min of the last row or the last column.
        '''
        # dp = [[0] * (len(grid)+1)] + [[0] + row for row in grid]
        if not grid:
            return
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[m-1][n-1]
# @lc code=end

grid = [[1,3,1], [1,5,1], [4,2,1]]
ans = Solution().minPathSum(grid)
print(ans)