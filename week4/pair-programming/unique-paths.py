#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
import unittest

class Solution:
    def uniquePaths_2d(self, m, n):
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths(self, m, n):
        # let the rows overwrite: after filling ith row, i-1 row is no longer needed, hence a single row is enough
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
# @lc code=end


class TestSolution(unittest.TestCase):
    def test_1(self):
        m, n = 3, 7
        ans = Solution().uniquePaths(m, n)
        expected = 28
        self.assertEqual(ans, expected)

    def test_2(self):
        m, n = 3, 2
        ans = Solution().uniquePaths(m, n)
        expected = 3
        self.assertEqual(ans, expected)

    def test_3(self):
        m, n = 3, 3
        ans = Solution().uniquePaths(m, n)
        expected = 6
        self.assertEqual(ans, expected)


if __name__ == "__main__":
    unittest.main()
