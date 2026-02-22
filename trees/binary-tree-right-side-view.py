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
            Time: O(n)
            Space: O(n)
        '''
        if not root:
            return []
        
        # final answer
        ans = []

        # queue to store nodes during BFS traversal
        que = deque()

        # storeing node, level
        que.append((root, 0))
        # tracking which level we processed last
        lastProcessed = -1

        # BFS traversal
        while que:
            levelSize = len(que)
            for _ in range(levelSize):
                node, level = que.popleft()

                # if right exists, then storing it
                if node.right:
                    que.append((node.right, level + 1))
                # also if left exists, add it too
                if node.left:
                    que.append((node.left, level + 1))

                # if the current node's level is not processed, meaning this is the first node of the level in the from the right side view, hence adding it and then setting lastProcessed to that level so that no other nodes from the same level get added in the answer
                if level > lastProcessed:
                    ans.append(node.val)
                    lastProcessed = level
        
        return ans

        '''
            https://leetcode.com/problems/binary-tree-right-side-view/
            Time: O(n)
            Space: O(n)
        '''
        # if not root:
        #     return []
        # cur = root
        # ans = []
        # que = deque()
        # que.append((root, 0))
        # level = 1
        # op_level = -1
        # total = 1
        # while que:
        #     j = 0
        #     tmp = 0
        #     while j < total: 
        #         cur, lvl = que.popleft()
        #         if lvl > op_level:
        #             ans.append(cur.val)
        #             op_level += 1
        #         if cur.right:
        #             que.append((cur.right, level))
        #             tmp += 1
        #         if cur.left:
        #             que.append((cur.left, level))
        #             tmp += 1
        #         j += 1
        #     level += 1
        #     total = tmp
        # return ans