#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubseq(s, t):
            i = j = 0
            while i < len(s) and j < len(t):
                i, j = i + (s[i] == t[j]), j + 1
            return i == len(s)
        res = ''
        for word in dictionary:
            if isSubseq(word, s):
                res = min(res, word, key=lambda x: (-len(x), x))
        return res
# @lc code=end

