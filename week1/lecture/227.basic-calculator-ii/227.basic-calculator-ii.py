#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
      '''
      intuition:
      use a stack to keep track of prev elements for future operations
      use a sign variable to indicate the last sign; by default it should be + because the sign is always one step behind. will show you why.
      a num variable to hold the result of the last calculation

      by default sign should be + because we need to initialize the stack with the very first element to begin with

      1. num to keep track of result of last operation. stack to store prev results. sign to keep track of the last sign
      2. if element is a number, update num
      3. if element is a sign, perform operation according to the last sign. then update sign and reset num to 0.
      4. if last index reached, do step 3.
      '''
      res = 0
      sign = '+'
      stack = []
      for i, char in enumerate(s):
          if char.isdigit():
              res = res * 10 + ord(char) - ord('0')
          if char in {'+', '-', '*', '/'} or i == len(s)-1:
              if sign == '+':
                  stack.append(res)
              elif sign == '-':
                  stack.append(-res)
              elif sign == '*':
                  stack.append(stack.pop() * res)
              else:
                  stack.append(int(stack.pop() / res))
              sign = char
              res = 0
      return sum(stack)
# @lc code=end

# s = "3+2*2"
# s = '3/2'
# s = "14-3/2"