'''
### intuition
greedily split the string, counting the occurences of balanced substrings on the fly:
R: +1
L: -1
increment res if count == 0
'''

#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s):
        count = res = 0
        for c in s:
            count += 1 if c == 'L' else -1
            res += count == 0
        return res
# @lc code=end

s = 'LLLLRRRR'
s = 'RLRRRLLRLL'
s = 'RLRRLLRLRL'
s = 'RLLLLRRRLR'
ans = Solution().balancedStringSplit(s)
print(ans)