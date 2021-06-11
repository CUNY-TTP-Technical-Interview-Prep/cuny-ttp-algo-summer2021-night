#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List
class Solution:
    def minSubArrayLen(self, s, nums):
        '''
        goal: find the min length of a subarray whose sum is at least s.
        intuition:
        two pointers: i and j. j is constantly moving to the righ while i moves only if s reaches zero or below zero. at each iteration, decrement s by nums[j]. once s hits zero or below, we've found a subarray nums[i:j+1] whose sum meets our condition. then, while the condition holds true, increment i to explore subarrays of shorter length.

        edge case:
        what if the target can never be reached by the total sum? do a mod at the end, should return 0.

        what if subarray is the entire array? len5 mod 5 is 0. set res to n + 1 and do mod (n+1) at the end
        '''
        res = len(nums) + 1
        i = 0
        for j in range(len(nums)):
            s -= nums[j]
            while s <= 0: 
                res = min(res, j-i+1)
                s += nums[i] 
                i += 1
        return res % (len(nums) + 1) # if no subarray was found, res remains the same as the initial value, then it will return 0. 
# @lc code=end

s = 7
nums = [2,3,1,2,4,3]
s = 15
nums = [1,2,3,4,5]
ans = Solution().minSubArrayLen(s, nums)
print(ans)