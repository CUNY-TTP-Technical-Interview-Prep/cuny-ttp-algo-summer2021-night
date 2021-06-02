# Using builtins, easiest solution
# Runtime: 32 ms, faster than 39.87% of python3 submissions
# Memory Usage: 14.3 MB, less than 32.25% of python3 submissions
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

# Custom implementation modifying ASCII values
# Runtime: 48 ms, faster than 39.87% of python3 submissions
# Memory Usage: 14.3 MB, less than 32.25% of python3 submissions
class Solution:
    def toLowerCase(self, s: str) -> str:
        # Converting uppercase letter to lowercase letter in ASCII means adding 32
        # A -> 65 and a -> 97, so 65 + 32 = 97
        # Z -> 90 and z -> 122, so 90 + 32 = 122
        #
        # Looping through each character of a string means O(n) time complexity
        # For this problem, constraint is 1 to 100 letters per string
        new_s = ''

        # Uppercase letter in ASCII ranges from 65 to 90 inclusive
        for ch in s:
            new_s += chr(ord(ch) + 32) if ord(ch) >= 65 and ord(ch) <= 90 else ch
        return new_s