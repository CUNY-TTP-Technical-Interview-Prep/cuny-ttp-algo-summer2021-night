#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#

# @lc code=start
from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        longest = ''
        seen = set([longest])
        for word in words:
            if word[:-1] in seen:
                seen.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest
# @lc code=end

