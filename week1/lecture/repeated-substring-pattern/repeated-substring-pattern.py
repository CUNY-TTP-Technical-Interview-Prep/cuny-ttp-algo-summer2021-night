class Solution:
  '''
  ### intuition
  - multiple copies of a substring == whole string
  - define i = initial length of the substring
  - n = length of the original string
  - while i < upper bound (n//2 + 1):
    if n is divisible i, check if substring multiplied by num of copies is valid or not?
      - return true early if found
    increment i
  return False
  '''
  def repeatedSubstringPattern(self, s: str) -> bool:
    i = 1
    n = len(s)
    while i < n // 2 + 1:
      # n // i returns the number of valid copies
      if n % i == 0 and s[:i] * (n // i) == s:
          return True
      i += 1
    return False