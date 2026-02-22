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

            NOTE: There are two approaches to track all the elements of the the current level,
            either do it with adding a NONE marker at the end of each level
            or track the size of the queue at the beginning of each level and pop that many elements

        '''
        if not root:
            return []
        ans = []

        que = deque()
        que.append(root)
        que.append(None)
        tmp = []
        while que:
            node = que.popleft()
            if node:
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            else:
                if que:
                    que.append(None)
                ans.append(tmp)
                tmp = []
        return ans

        # if not root:
        #     return []
        # que = deque([root])
        # ans = list()
        # total = 1
        # while que:
        #     t = []
        #     j = 0
        #     tmp = 0
        #     while que and j < total:
        #         cur = que.popleft()
        #         t.append(cur.val)
        #         if cur.left:
        #             que.append(cur.left)
        #             tmp += 1
        #         if cur.right:
        #             que.append(cur.right)
        #             tmp += 1
        #         j += 1
        #     total = tmp
        #     if t:
        #         ans.append(t)
        # return ans