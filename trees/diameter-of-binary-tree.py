# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            https://leetcode.com/problems/diameter-of-binary-tree/description/
            Time: O(n)
            Space: O(h)
        '''
        maxi = [0]
        def height(root):
            if root:
                left = height(root.left)
                right = height(root.right)
                maxi[0] = max(left + right, maxi[0])
                return max(left, right) + 1
            return 0
        
        height(root)
        return maxi[0]