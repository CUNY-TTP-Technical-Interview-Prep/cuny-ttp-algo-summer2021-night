#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    '''
    map each integer to its frequency.
    sort the map first by frequency count then by the key.
    '''
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        # res = []
        # for k, v in sorted(count.items(), key=lambda x: (x[1], -x[0])):
        #     res.extend([k] * v)
        # return res
        return sorted(nums, key=lambda x: (count[x], -x))
# @lc code=end

nums = [2,3,1,3,2]
nums = [1,1,2,2,2,3]
Sol = Solution()
ans = Sol.frequencySort(nums)
print(ans)