# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        '''
            https://leetcode.com/problems/binary-tree-level-order-traversal/
            Time: O(n)
            Space: O(n)
        '''
        if not root:
            return []
        que = deque([root])
        ans = list()
        total = 1
        while que:
            t = []
            j = 0
            tmp = 0
            while que and j < total:
                cur = que.popleft()
                t.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                    tmp += 1
                if cur.right:
                    que.append(cur.right)
                    tmp += 1
                j += 1
            total = tmp
            if t:
                ans.append(t)
        return ans