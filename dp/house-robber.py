class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/house-robber/
            Time: O(n)
            Space: O(1)

            These are two different approaches, BOTH WORK.
            First one makes changes in the original array and
            2nd one doesn't do that
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # if n == 3:
        #     return max(nums[0] + nums[2], nums[1])
        # maxi = max(nums[0], nums[1])
        # nums[2] = max(nums[0] + nums[2], nums[1])
        # for i in range(3, n):
        #     nums[i] = maxi + nums[i]
        #     maxi = max(nums[i - 2], nums[i - 1])
        # return max(maxi, nums[n - 1])

        '''
            Time: O(n)
            Space: O(1)
        '''
        prev_max = nums[0]
        maxi = max(nums[0], nums[1])
        for i in range(2, n):
            maxi, prev_max = max(nums[i] + prev_max, maxi), maxi
        return maxi