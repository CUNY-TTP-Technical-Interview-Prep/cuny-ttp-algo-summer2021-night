#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        '''
        intuition: the longest prefix that all these words share cannot exceed the length of the shortest word. 
        
        logic: 
        find the shortest word.
        traverse that word from left to right with pointer i. for each i, scan each word in array, if word[i] is not equal to shortest[i], we can exit early and return the existing prefix: shortest[:i]
        '''

        if not strs: return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for item in strs:
                if item == shortest: continue
                if item[i] != char:
                    return shortest[:i]
        return shortest
# @lc code=end

strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
ans = Solution().longestCommonPrefix(strs)
print(ans)