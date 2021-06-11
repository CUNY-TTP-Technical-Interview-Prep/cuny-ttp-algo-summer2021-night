#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
from collections import Counter
from typing import List
class Solution:
    '''
    time: o(n + 101^2)
    space: o(101)

    The mathematical formula is combination formula. When you need to select 3 numbers from 'n' numbers, no ways of doing it is nC3 which is basically n * (n-1) * (n-2)/6, similarly when you need to select 2 numbers from 'n' numbers, the number of ways of doing it is nC1 which is equal to n * (n-1) / 2.
    '''
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        res = 0
        for i in count:
            for j in count:
                k = target - i - j
                if i == j == k:
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j:
                    res += count[i] * (count[i] - 1) // 2 * count[k]
                elif i < j < k:
                    res += count[i] * count[j] * count[k]
        return res % (10**9 + 7)
# @lc code=end

arr = [1,1,3]
target = 5
arr = [1,1,2,2,2,2]; target = 5
arr = [1,1,2,2,3,3,4,4,5,5]; target = 8
arr = [2,1,3]
target = 6
sol = Solution()
res = sol.threeSumMulti(arr, target)
print(res)