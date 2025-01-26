import heapq as hq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, arr: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            Time: O(k) + O(nlogk) ~= O(nlogk)
            Space: O(k)
        '''
        hps = list()
        for i, lst in enumerate(arr):
            if lst:
                hps.append(tuple([lst.val, i, lst]))
        hq.heapify(hps)
        if hps:
            smallest_value, i, node = hq.heappop(hps)
            head = ListNode(smallest_value)
            nxt = node.next
            if nxt:
                hq.heappush(hps, tuple([nxt.val, i, nxt]))
        else:
            head = None
        ans = head

        while hps:
            smallest_value, i, node = hq.heappop(hps)
            ans.next = ListNode(smallest_value)
            ans = ans.next
            nxt = node.next
            if nxt:
                hq.heappush(hps, tuple([nxt.val, i, nxt]))

        return head

        '''
            Time: O(k) + O(nlogk) ~= O(nlogk)
            Space: O(n) + O(k) ~= O(n)
        '''
        # hps = list()
        # store = dict()
        # for i, lst in enumerate(arr):
        #     if lst:
        #         hps.append(tuple([lst.val, i]))
        #         store[tuple([lst.val, i])] = lst
        # hq.heapify(hps)
        # if hps:
        #     smallest_value = hq.heappop(hps)
        #     head = ListNode(smallest_value[0])
        #     cur_element = store[smallest_value]
        #     nxt = cur_element.next
        #     if nxt:
        #         hq.heappush(hps, tuple([nxt.val, smallest_value[1]]))
        #         store.pop(smallest_value)
        #         store[tuple([nxt.val, smallest_value[1]])] = nxt
        # else:
        #     head = None
        # ans = head

        # while hps:
        #     smallest_value = hq.heappop(hps)
        #     ans.next = ListNode(smallest_value[0])
        #     ans = ans.next
        #     cur_element = store[smallest_value]
        #     nxt = cur_element.next
        #     if nxt:
        #         hq.heappush(hps, tuple([nxt.val, smallest_value[1]]))
        #         store.pop(smallest_value)
        #         store[tuple([nxt.val, smallest_value[1]])] = nxt

        # return head