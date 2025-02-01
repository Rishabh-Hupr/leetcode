class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
            https://leetcode.com/problems/move-zeroes/description/
            NOTE: USING 2 Pointers
            Time: O(n)
            Space: O(1)
        '''
        # i = 0
        # j = 1
        n = len(nums)
        # while j < n and  i < j:
        #     if not nums[i]:
        #         while j < n and not nums[j]:
        #             j += 1
        #         if j < n:
        #             nums[i], nums[j] = nums[j], nums[i]
        #     j += 1
        #     i += 1
        
        '''
            NOTE: Using 2 Pointers
            Time: O(n)
            Space: O(1)
        '''
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        