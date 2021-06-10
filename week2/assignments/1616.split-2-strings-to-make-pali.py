class Solution:
  '''
  scan the string with two pointers i and j.
  keep incrementing/decrementing if they match.
  at the first mismatch, check for the two substrings in both a and b:
    1. a[i:j+1]
    2. b[i:j+1]
  because we are not sure which of the two should take up the body of the ultimate palindrome formation
  the goal is to see if this substr is a palindrome as well.
  
  perform the steps on both a and b
  1. a[prefix] + b[suffix]
  2. b[prefix] + a[suffix]

  a = "abdef", b = "fecab"
  fec + ef
  or fe + def
  substrs in between: c or d
  '''
  def checkPalindromeFormation(self, a: str, b: str) -> bool:
    def isPali(s, i, j):
      while i < j:
        if s[i] != s[j]:
          return False
        i += 1
        j -= 1
      return True
    
    def check(a, b):
      i, j = 0, len(a)-1
      while i < j:
        if a[i] != b[j]:
          return isPali(a, i, j) or isPali(b, i, j)
        i += 1
        j -= 1
      return True
    
    return check(a,b) or check(b,a)

a = "xbdef"
b = "xecab"
a, b = 'y', 'x'
a = "ulacfd"
b = "jizalu"
a = "abddef"
b = "fecxab"
a = "pvhmupgqeltozftlmfjjde"
b = "yjgpzbezspnnpszebzmhvp"
Sol = Solution()
ans = Sol.checkPalindromeFormation(a, b)
print(ans)