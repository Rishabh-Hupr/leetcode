# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            https://leetcode.com/problems/merge-two-sorted-lists/description/
            Time: O(m+n)
            Space: O(1)
        '''
        if list1 and list2:
            head = None
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next

            cur = head
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            while list1:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            while list2:
                cur.next = list2
                list2 = list2.next
                cur = cur.next


            return head
        else:
            return list1 or list2 or None
