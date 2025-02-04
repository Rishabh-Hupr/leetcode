class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/maximum-ascending-subarray-sum/?envType=daily-question&envId=2025-02-04
            Time: O(n)
            Space: O(1)
        '''
        j = 1
        cur = maxi = nums[0]
        n = len(nums)
        while j < n:
            if nums[j] > nums[j - 1]:
                cur += nums[j]
            else:
                maxi = max(maxi, cur)
                cur = nums[j]
            j += 1
        return max(maxi, cur)
            