# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        '''
            https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
            Time: O(n)
            Space: O(n)
        '''
        ans = []
        if not root:
            return ans
        que = deque()
        que.append(root)
        item = 1
        while que:
            j = 0
            tmp = 0
            tmp_lst = []
            while j < item:
                cur = que.popleft()
                tmp_lst.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                    tmp += 1
                if cur.right:
                    que.append(cur.right)
                    tmp += 1
                j += 1
            item = tmp
            ans.append(tmp_lst)
        ans.reverse()
        return ans