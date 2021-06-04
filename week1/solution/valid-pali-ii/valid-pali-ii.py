#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    '''
    intuition:
    at most one character does not belong to the otherwise valid palindrome. scan the string using two pointers. update left/right at end of each iteration. if left and right don't match, try removing either left or right and determine if the resulting substrings are a palindrome; if left makes a pali, then the right char should be removed. if neither substrings are valid, return False.
    '''
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        def isPali(s, i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return isPali(s, i+1, j-1)
        while i < j:
            if s[i] != s[j]:
                left, right = s[i:j], s[i+1:j+1]
                return isPali(left, 0, len(left)-1) or isPali(right, 0, len(right)-1)
            i += 1
            j -= 1
        return True
# @lc code=end

s = "aba"
s = "abccxba"
Sol = Solution()
ans = Sol.validPalindrome(s)
print(ans)