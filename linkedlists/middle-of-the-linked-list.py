# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            https://leetcode.com/problems/middle-of-the-linked-list/
            Time: O(n//2) ~ O(n)
            Space: O(1)
        '''
        slow = head
        fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        return slow