# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
            https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
            Time: O(n)
            Space: O(n)
            NOTE: Missed to check the constraint on the lowset possible sum, had initialized tmp to 0 initially, but one failure reminded me to initialize it to float('-inf')
        '''
        que = deque()
        que.append(root)
        maxSum = -10**5 - 1 # stores the maximum sum found so far per level
        ans = 1 # stores the level where the sum was found
        level = 1
        while que:
            levelSize = len(que)
            tmp = 0
            for _ in range(levelSize):
                node = que.popleft()
                tmp += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if tmp > maxSum:
                maxSum = tmp
                ans = level
            level += 1

        return ans
