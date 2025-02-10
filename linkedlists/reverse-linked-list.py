# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            https://leetcode.com/problems/reverse-linked-list/
            Time: O(n)
            Space: O(1)
        '''
        prev = None
        tmp = head
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev