"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
            https://leetcode.com/problems/copy-list-with-random-pointer/
            Time: O(n)
            Space: O(n)
            NOTE: without modifying the original list
        '''
        if not head:
            return None
        store = defaultdict(dict)
        new_head = Node(head.val)
        store[head.val][id(head)] = new_head
        if head.random:
            if head.random.val in store and id(head.random) in store[head.random.val]:
                    new_head.random = store[head.random.val][id(head.random)]
            else:
                one_more = Node(head.random.val)
                new_head.random = one_more
                store[head.random.val][id(head.random)] = one_more
        cur = new_head
        head = head.next
        while head:
            new_node = None
            if head.val not in store or id(head) not in store[head.val]:
                new_node = Node(head.val)
                store[head.val][id(head)] = new_node
            else:
                new_node = store[head.val][id(head)]
            if head.random:
                if head.random.val in store and id(head.random) in store[head.random.val]:
                    new_node.random = store[head.random.val][id(head.random)]
                else:
                    one_more = Node(head.random.val)
                    new_node.random = one_more
                    store[head.random.val][id(head.random)] = one_more
            cur.next = new_node
            cur = cur.next
            head = head.next
        return new_head
        