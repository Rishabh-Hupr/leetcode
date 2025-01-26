import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            I have written 2 solutions here, use one at a time
        '''
        # # space O(1)
        # # time O(n) + O(n) + O(klogn)
        # for i, val in enumerate(nums):
        #     nums[i] = -val
        # hq.heapify(nums)
        # for i in range(k-1):
        #     hq.heappop(nums)
        # return -hq.heappop(nums)
        # space O(k)
        # time O(k) + O(k) + O((n-k)log(k))
        hps = list()
        for i in range(k):
            hps.append(nums[i])
        hq.heapify(hps)
        n = len(nums)
        for i in range(k, n):
            if nums[i] > hps[0]:
                hq.heapreplace(hps, nums[i])
        return hps[0]
