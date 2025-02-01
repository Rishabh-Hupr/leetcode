class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/maximum-subarray/description/
            Time: O(n)
            Space: O(1)
        '''
        n = len(nums)
        cur = nums[0]
        ans = nums[0]
        for i in range(1, n):
            cur = max(nums[i] + cur, nums[i])
            ans = max(ans, cur)
        return ans
