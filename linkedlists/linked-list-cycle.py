# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            https://leetcode.com/problems/linked-list-cycle/
            Time: O(n)
            Space: O(1)
        '''
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if id(slow) == id(fast):
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        return False
