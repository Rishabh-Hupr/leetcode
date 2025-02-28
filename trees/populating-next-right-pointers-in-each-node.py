"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
            https://leetcode.com/problems/populating-next-right-pointers-in-each-node
            Time: O(n)
            Space: O(n)
        '''
        if not root:
            return None
        que = deque()
        que.append(root)
        level = 0
        while que:
            j = 0
            while j < 2 ** level:
                cur = que.popleft()
                if j+1 != 2**level and que:
                    cur.next = que[0]
                if cur.left:
                    que.append(cur.left)
                    que.append(cur.right)
                j += 1
            level += 1
        return root