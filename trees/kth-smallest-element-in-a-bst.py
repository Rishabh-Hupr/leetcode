# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            Time: O(n)
            Space: O(h), h ~ height of tree
        '''
        def inorder(node):
            nonlocal k
            if not node:
                return None
            
            ans = inorder(node.left)
            if ans is not None:
                return ans
            k -= 1
            if not k:
                return node.val
            return inorder(node.right)
        
        return inorder(root)
