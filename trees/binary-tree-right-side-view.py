from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            https://leetcode.com/problems/binary-tree-right-side-view/
            Time: O(n)
            Space: O(n)
        '''
        if not root:
            return []
        cur = root
        ans = []
        que = deque()
        que.append((root, 0))
        level = 1
        op_level = -1
        total = 1
        while que:
            j = 0
            tmp = 0
            while j < total: 
                cur, lvl = que.popleft()
                if lvl > op_level:
                    ans.append(cur.val)
                    op_level += 1
                if cur.right:
                    que.append((cur.right, level))
                    tmp += 1
                if cur.left:
                    que.append((cur.left, level))
                    tmp += 1
                j += 1
            level += 1
            total = tmp
        return ans