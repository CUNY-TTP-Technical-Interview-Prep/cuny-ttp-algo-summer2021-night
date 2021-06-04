#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
  '''
  ### intuition
  declare hashmap mapping left to right
  use a stack to record the opening brackets
  scan the string: 
  if char is a key, append to stack
  elif char is a closing bracket:
    1. if stack not empty check if last element, popped, is a matching opening: if not return False
    2. if stack is empty return False
  in the end stack should be empty
  '''
  def isValid(self, s: str) -> bool:
    braces = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
      if char in braces:
          stack.append(char)
      elif not stack or braces[stack.pop()] != char:
          return False
    return not stack
# @lc code=end

Sol = Solution()
s = '()'
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
s = '['
s = ']'
ans = Sol.isValid(s)
print(f'ans: {ans}')