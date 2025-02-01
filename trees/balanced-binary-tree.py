# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        https://leetcode.com/problems/balanced-binary-tree/
        Time: O(n)
        Space: O(h)
    '''
    def height_balance(self, root):
        if root:
            left = self.height_balance(root.left)
            if left[1]:
                right = self.height_balance(root.right)
            else:
                return (left[0] + 1, False)
            print(root.val, left, right)
            if left[1] and right[1]:
                if abs(left[0] - right[0]) > 1:
                    return (max(left[0], right[0]) + 1, False)
                else:
                    return (max(left[0], right[0]) + 1, True)
            else:
                return (max(left[0], right[0]) + 1, False)
        return (0, True)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height_balance(root)[1]