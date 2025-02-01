import heapq as hq

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # hq.heapify(nums)
        # print(nums)
        # ans = 1
        # n = 0
        # for i in nums:
        #     n += 1
        #     if i==ans:
        #         ans += 1
        # for i in range(n-1, -1, -1):
        #     if nums[i] == ans:
        #         ans += 1
        # return ans
        # j = n - 1
        # i = 0
        # while i <= j:
        #     if nums[i] <= 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         nums.pop()
        #         j -= 1
        #     i += 1

        '''
            https://leetcode.com/problems/first-missing-positive/description/
            Time: O(n)
            Space: O(1)
            DESCRIPTION
                We do a cyclic sort algorithm, placing numbers in the arrays
                length range on the respective indexes
        '''

        n = len(nums)
        i = 0
        while i < n:
            val = nums[i]
            if 1<= val <= n:
                if val != i+1 and nums[val - 1] != nums[i]:
                    nums[val-1], nums[i] = val, nums[val-1]
                    continue
            i += 1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        # hq.heapify(nums)
        # print(nums)