#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    '''
    intuition: two pointers. start matching with i and j. at the first mismatch, move i back to i-j+1, the next index of the first match, and reset j to 0 to restart the process
    '''
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        if m < n: return -1
        if not n: return 0
        i = j = 0
        while i < m and j < n:
            if haystack[i] != needle[j]:
                i = i-j+1
                j = 0
            else:
                i += 1
                j += 1
        return i-j if j == len(needle) else -1

# @lc code=end

haystack = "aaaaa"
needle = "bba"
haystack = "hello"
needle = "ll"
haystack = 'hudstrxstrawberry'
needle = 'straw'
ans = Solution().strStr(haystack, needle)
print(ans)