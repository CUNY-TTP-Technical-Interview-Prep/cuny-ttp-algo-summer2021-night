#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for char in s:
            val = ord(char)
            if 65 <= val <= 90:
                res.append(chr(val + 32))
            else:
                res.append(char)
        return ''.join(res)

# @lc code=end

s = 'LovelY'
ans = Solution().toLowerCase(s)
print(ans)

print(ord('a'))