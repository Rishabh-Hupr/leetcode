# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
            Time: O(n)
            Space: O(n)
        '''
        if not root:
            return []

        ans = []

        que = deque()
        direction = True # true represents left -> right, false represents right -> left

        que.append(root)
        
        while que:
            levelSize = len(que)
            tmp = []
            for _ in range(levelSize):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if direction:
                ans.append(tmp)
            else:
                ans.append(tmp[::-1])
            direction = not direction
        
        return ans
