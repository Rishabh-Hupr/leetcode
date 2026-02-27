# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
            https://leetcode.com/problems/find-largest-value-in-each-tree-row/
            Time: O(n)
            Space: O(n)

            NOTE: Missed to check the constraint on the lowset possible value, had initialized tmp to 0 initially, but one failure reminded me to initialize it to float('-inf')
        '''
        if not root:
            return []
        
        ans = []
        que = deque()
        que.append(root)
        
        while que:
            levelSize = len(que)
            tmp = float('-inf')
            for _ in range(levelSize):
                node = que.popleft()
                tmp = max(tmp, node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(tmp)
        return ans
