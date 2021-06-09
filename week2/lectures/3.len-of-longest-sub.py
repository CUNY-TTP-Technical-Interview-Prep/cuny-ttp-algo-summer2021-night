#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = res = 0
        count = {}
        for j, char in enumerate(s):
            if char in count and i <= count[char]:
                i = count[char] + 1
            else:
                res = max(res, j-i+1)
            count[char] = j
        return res
# @lc code=end

