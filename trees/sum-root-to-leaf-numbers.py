# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''
            https://leetcode.com/problems/sum-root-to-leaf-numbers/
            Time: O(n)
            Space: O(logn)
        '''
        stk = []
        stk.append([root, 0])
        ans = 0
        while stk:
            cur, lst_sum = stk.pop()
            lst_sum *= 10
            lst_sum += cur.val
            if not cur.left and not cur.right:
                ans += lst_sum
                continue
            if cur.left:
                stk.append([cur.left, lst_sum])
            if cur.right:
                stk.append([cur.right, lst_sum])
        return ans
