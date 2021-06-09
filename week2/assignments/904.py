#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, tree): # o(n); o(1)
        lastFruit = secondLastFruit = -1
        _max = currMax = lastFruitCount = 0
        for fruit in tree:
            if fruit == lastFruit or fruit == secondLastFruit:
                currMax += 1
            else:
                currMax = lastFruitCount + 1 # last fruit count + new fruit

            if fruit == lastFruit:
                lastFruitCount += 1
            else:
                lastFruitCount = 1
                secondLastFruit, lastFruit = lastFruit, fruit
            
            _max = max(_max, currMax)
        return _max

    def totalFruit2(self, tree): # o(n); o(n)
        '''
        intuition: sliding window.
        '''
        count = {}
        i = res = 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res

# @lc code=end

tree = [1,2,1]
tree = [0,1,2,2]
tree = [3,3,3,1,2,1,1,2,3,3,4]
tree = [1,2,3,2,2]
ans = Solution().totalFruit(tree)
print(ans)