#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        rome = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = []
        for k, v in rome.items():
            res.append(num // k * v)
            num %= k
        return ''.join(res)

        # val = [1000,900,500,400,100,90,50,40,10,9,8,7,6,5,4,3,2,1]
        # rom = ["M","CM","D","CD","C","XC","L","XL","X","IX",'VIII','VII','VI',"V","IV","III",'II','I']
        # res = []
        # for num in numbers:
        #     curr = []
        #     i = 0
        #     while num:
        #         curr.append(num // val[i] * rom[i])
        #         num %= val[i]
        #         i += 1
        #     res.append(''.join(curr))
        # return res
# @lc code=end

Sol = Solution()
testcases = [3, 4, 9, 58, 1994]
ans = [Sol.intToRoman(num) for num in testcases]
print(ans)