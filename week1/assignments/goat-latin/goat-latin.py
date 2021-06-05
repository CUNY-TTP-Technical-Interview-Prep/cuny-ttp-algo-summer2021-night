#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        res = []
        for i, word in enumerate(sentence.split(), 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ma' + 'a' * i
            res.append(word)
        return ' '.join(res)
# @lc code=end

Sol = Solution()
sentence = "I speak Goat Latin"
sentence = "The quick brown fox jumped over the lazy dog"
ans = Sol.toGoatLatin(sentence)
print(ans)
