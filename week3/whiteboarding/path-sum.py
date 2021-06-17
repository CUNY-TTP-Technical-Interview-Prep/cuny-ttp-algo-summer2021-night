# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    define a helper function that helps me traverse the tree recursively while keeping track of the current sum.
    compare curr sum to target only if i reach the leaf
    dfs helper func accepts 2 params: prev, node
        - prev: stores previous result of existing path
        - node: curr node
        - base case: if node is null, return False
        - if leaf node: compare current sum with target.
        - keep on calling dfs to explore left and right
    '''
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(prev, node):
            if not node: return False
            # accumulate sum on the existing path
            curr = prev + node.val
            if not (node.left or node.right):
                return curr == targetSum
            # recursively call func on left and right to exhaust the path
            return dfs(curr, node.left) or dfs(curr, node.right)
        return dfs(0, root)