#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign *= -1
            x = -x
        y = 0
        while x:
            y = y * 10 + x % 10 # get the remainder of the division with modulo 10. move it to the front
            x //= 10 # update x with the quotient of the division as it will be carried to the next iteration
        y *= sign
        return y if -(2**31) < y < 2**31-1 else 0
# @lc code=end

x = 1534236469
ans = Solution().reverse(x)
print(ans)