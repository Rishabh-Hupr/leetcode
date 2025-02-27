class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
            Time: O(n)
            Space: O(1)
        '''
        pre_min = pre_max = cur = res = 0
        for i in nums:
            cur += i
            res = max(abs(cur - pre_max), abs(cur - pre_min), res)
            pre_max = max(pre_max, cur)
            pre_min = min(pre_min, cur)
        return res