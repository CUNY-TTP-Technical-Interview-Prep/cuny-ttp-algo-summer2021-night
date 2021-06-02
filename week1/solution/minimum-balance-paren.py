'''
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
Given a string s of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
Example
Input: s = "())"
Output: 1
'''
def minAddToMakeValid(self, s: str) -> int:
    # we will only ever push '(' to stack, so this stack is to keep track of opening bracket only. The variable is to keep track of the length of the stack.
    stack = 0
    # count is to keep track of trailing closing brackets
    count = 0
    # iterate through each char of string
    for c in s:
        # if c is '(', push in stack, so increase the stack count
        if c == '(':
            stack += 1
        # if c is ')' and stack is not empty, we can now pop 1 out of the stack,
        # so subtract from stack
        elif c == ')' and stack > 0:
            stack -= 1
        # if stack is empty and we run into ')', we need to add to count
        else:
            count+=1
    # return whatever is left in the stack w/o the matching bracket, and the trailing closing bracket
    return stack + count
