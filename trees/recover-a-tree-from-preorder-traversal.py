# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        '''
            https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
            Time: O(n)
            Space: O(n)
        '''

        # curating number
        def curate_number(i, n):
            num = 0
            while i < n and traversal[i] != "-":
                num += int(traversal[i])
                num *= 10
                i += 1
            num //= 10
            return (num, i)

        stk = []
        n = len(traversal)
        i = 0
        c = 0

        # rooting tree
        num, i = curate_number(i, n)
        root = TreeNode(num)
        
        cur = root
        stk.append((root, 0))

        while i < n:
            if traversal[i] != "-":

                # curating number
                num, i = curate_number(i, n)
                new_node = TreeNode(num)
                
                # main logic of using stack to keep track of left and right nodes
                if c > stk[-1][1]:
                    stk[-1][0].left = new_node
                else:
                    while c <= stk[-1][1]:
                        stk.pop()
                    stk[-1][0].right = new_node

                stk.append((new_node, c))
                c = 0
            else:
                c += 1
                i += 1


        return root
