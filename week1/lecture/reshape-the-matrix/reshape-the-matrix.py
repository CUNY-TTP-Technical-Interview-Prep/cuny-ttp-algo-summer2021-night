#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * c for _ in range(r)]
        if m == r and n == c or m * n != r * c: return mat
        for i in range(m):
            for j in range(n):
                x = i*n + j
                a, b = x//c, x%c
                res[a][b] = mat[i][j]
        return res
# @lc code=end

mat = [[1,2],[3,4]]
r = 1
c = 4
mat = [[1,2],[3,4]]
r = 2
c = 4
mat = [[1,2]]
r = 1
c = 1
Sol = Solution()
ans = Sol.matrixReshape(mat, r, c)
print(f'ans: {ans}')