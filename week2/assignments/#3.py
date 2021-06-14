#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    '''
    intuition:
    two pointers i and j to move name / typed.
    - j moves constantly from left to right. 
    - i is incremented only if name[i] matches typed[j] and if i hasn't reached len of name
    - a mismatch can be excused (because of the long press) only if typed[j] is same as the previously typed char = typed[j-1].
        - return False if the mismatch found at the very beginning
        - or if curr char is not long pressed
    - at the end return boo of i successfully reaching its end
    '''
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j==0 or typed[j] != typed[j-1]:
                return False
        return i == len(name)
# @lc code=end

name = "leelee"
typed = "lleeelee"
name = "laiden"
typed = "laiden"
name = "alex"
typed = "aaleex"
name = "saeed"
typed = "ssaaedd"
Sol = Solution()
ans = Sol.isLongPressedName(name, typed)
print(ans)