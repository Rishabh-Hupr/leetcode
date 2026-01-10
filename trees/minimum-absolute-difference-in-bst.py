# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
            Time: O(n)
            Space: O(h) -
                where h = height of tree, 
                h ~~ log(n), if it is balanced binary tree
                h ~~ n, if it is a skewed tree
        '''
        ans = [10**5 + 1]
        prev = [None]

        def fun(node):
            if not node:
                return

            fun(node.left)
            if prev[0] is not None:
                ans[0] = min(ans[0], node.val - prev[0])
            prev[0] = node.val
            fun(node.right)

        
        fun(root)
        return ans[0]
