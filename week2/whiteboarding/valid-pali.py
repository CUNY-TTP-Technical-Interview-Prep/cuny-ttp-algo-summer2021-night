#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower(): return False
                i += 1
                j -= 1
        return True
# @lc code=end

s = "A man, a plan, a canal: Panama"
Sol = Solution()
ans = Sol.isPalindrome(s)
print(ans)