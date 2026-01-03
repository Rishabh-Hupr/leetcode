# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            Time: O(n * m)
            Space: O(max(n, m))

            NOTE: It has both recursive solution and the iterative solution using the stack approach
            Recursive approach is commented out
            Gonna try the hashing approach.

            Time reported was 37ms at best for 185 test cases
        '''
        def check_subTree(r, s):
            if not r and not s:
                return True
            stk = [(r, s)]
            while stk:
                root, subRoot = stk.pop()
                if not root and not subRoot:
                    continue
                if not root or not subRoot:
                    return False
                
                if root.val == subRoot.val:
                    stk.append((root.right, subRoot.right))
                    stk.append((root.left, subRoot.left))
                else:
                    return False
                
            return True
        
        # if not root and not subRoot:
        #     return True
        # if not root or not subRoot:
        #     return False
        # if check_subTree(root, subRoot):
        #     return True

        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        if not root or not subRoot:
            return False

        stk = [root]
        while stk:
            r = stk.pop()
            if check_subTree(r, subRoot):
                return True
            
            if r:
                stk.append(r.right)
                stk.append(r.left)
        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            Time: O(n + m)
            Space: O(n + m)

            NOTE: This is hashing approach, the best one from Time perspective, the time was: 8ms for 185 test cases
        '''
        store_root = {}
        def hash(node, store):
            if not node:
                return "#"
            store[node] = f"({node.val},{hash(node.left, store)},{hash(node.right, store)})"
            return store[node]

        def hash_subroot(node):
            if not node:
                return "#"
            return f"({node.val},{hash_subroot(node.left)},{hash_subroot(node.right)})"
        
        hash(root, store_root)
        subroot_hash = hash_subroot(subRoot)
        if subroot_hash in store_root.values():
            return True
        return False
