#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
  '''
  intuition: two pointers. flip chars on either side and increment i and j only if they're both letters. otherwise if one of them is not a letter, increment i or j.
  '''
  def reverseOnlyLetters(self, s: str) -> str:
    i, j = 0, len(s)-1
    res = list(s)
    while i < j:
      if not s[i].isalpha():
        i += 1
      elif not s[j].isalpha():
        j -= 1
      else:
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1
      return ''.join(res)
# @lc code=end

s = "ab-cd"
s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
Sol = Solution()
ans = Sol.reverseOnlyLetters(s)
print(ans)
assert ans == "Qedo1ct-eeLg=ntse-T!"