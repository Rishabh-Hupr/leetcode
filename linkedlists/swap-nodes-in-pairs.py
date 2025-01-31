# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Time: O(n)
            Space: O(1)
        '''
        if not head or not head.next:
            return head
        prev = cur = head
        next = head.next
        head = head.next

        while cur and next:
            prev.next, cur.next, next.next = cur.next, next.next, cur
            prev = cur
            cur = cur.next
            if cur:
                next = cur.next
        return head