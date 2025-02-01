import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            https://leetcode.com/problems/kth-largest-element-in-an-array/description/
            I have written 2 solutions here, use one at a time
            Time: O(n) + O(n) + O(klogn)
            Space: O(1)
        '''
        # for i, val in enumerate(nums):
        #     nums[i] = -val
        # hq.heapify(nums)
        # for i in range(k-1):
        #     hq.heappop(nums)
        # return -hq.heappop(nums)
        
        '''
            Time: O(k) + O(k) + O((n-k)log(k))
            Space: O(k)
        '''
        hps = list()
        for i in range(k):
            hps.append(nums[i])
        hq.heapify(hps)
        n = len(nums)
        for i in range(k, n):
            if nums[i] > hps[0]:
                hq.heapreplace(hps, nums[i])
        return hps[0]
