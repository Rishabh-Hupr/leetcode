import heapq as hq
class Solution:
    def minOperations(self, hps: List[int], k: int) -> int:
        '''
            https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii
            Time: O(nlogn)
            Space: O(1)
        '''
        hq.heapify(hps)
        ans = 0
        while hps[0] < k:
            fs = hq.heappop(hps)
            sc = hq.heappop(hps)
            res = fs * 2 + sc
            hq.heappush(hps, res)
            ans += 1
        return ans