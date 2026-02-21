# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
            The idea is to use a depth first search to calculate the maximum path sum for each node.
            We will keep track of the maximum path sum we have seen so far and update it whenever we find a new maximum.

            https://leetcode.com/problems/binary-tree-maximum-path-sum/
            Time: O(n) where n is the number of nodes in the tree, since we visit each node once.
            Space: O(h) where h is the height of the tree, since we use a recursive stack that can go as deep as the height of the tree.
        '''
        ans = float('-inf')
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            ans = max(node.val + left + right, ans)

            return node.val + max(left, right)
        
        dfs(root)
        return ans
