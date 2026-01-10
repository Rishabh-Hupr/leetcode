# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            NOTE: Recursive solution
            Time: O(h)
            Space: O(h)
                where h = height of tree
                if balanced, h = log(n)
                if skewed, h = n
        '''
        # if not root:
        #     return None
        # if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
        #     return root
        
        # if root.val >= p.val and root.val >= q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        
        '''
            NOTE: Iterative solution
            Time: O(h)
            Space: O(1)
                where h = height of tree
                if balanced, h = log(n)
                if skewed,  h = n
        '''
        while root:
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            elif root.val >= p.val and root.val >= q.val:
                root = root.left
            else:
                root = root.right
