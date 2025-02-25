from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        '''
            https://leetcode.com/problems/average-of-levels-in-binary-tree/
            Time: O(n)
            Space: O(n)
        '''
        que = deque()
        que.append(root)
        ite = 1
        ans = []
        while que:
            tmp_sum = 0
            j = 0
            tmp = 0
            while que and j < ite:
                pop_elem = que.popleft()
                tmp_sum += pop_elem.val
                if pop_elem.left:
                    que.append(pop_elem.left)
                    tmp += 1
                if pop_elem.right:
                    que.append(pop_elem.right)
                    tmp += 1
                j += 1
            ite = tmp
            if j:
                ans.append(tmp_sum / j)
        return ans
                