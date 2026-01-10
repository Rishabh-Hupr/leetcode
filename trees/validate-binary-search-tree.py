# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            NOTE: Recursive solution

            Time: O(n)
            Space: O(h), where h ~~ height of tree:
                h = log(n), if it is a balanced tree
                h = n, if it is a skewed tree
        '''
        # ans, prev = True, None
        # def dfs(root):
        #     if not root:
        #         return
            
        #     nonlocal ans, prev
            
        #     dfs(root.left)

        #     if prev is not None and root.val <= prev:
        #         ans = False
        #     if not ans:
        #         return
        #     prev = root.val

        #     dfs(root.right)
                

        # dfs(root)
        # return ans


        '''
            NOTE: Iterative solution with stack
            Time: O(n)
            Space: O(h), where h ~~ height of tree:
                h = log(n), if it is a balanced tree
                h = n, if it is a skewed tree
        '''
        prev = None
        stk = []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                if prev is not None:
                    if root.val <= prev:
                        return False
                prev = root.val
                root = root.right
        return True
