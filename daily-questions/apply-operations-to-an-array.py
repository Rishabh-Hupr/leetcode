class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        '''
            https://leetcode.com/problems/apply-operations-to-an-array/
            Time: O(n)
            Space: O(1)
        '''
        n = len(nums)
        zero_index = None
        for i in range(n-1):
            if not nums[i] and zero_index == None:
                zero_index = i
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                if zero_index == None:
                    zero_index = i + 1
        i = 0
        follow = 0
        while i < n:
            if nums[i]:
                if i != follow:
                    nums[i], nums[follow] = nums[follow], nums[i] 
                follow += 1
            i += 1

        return nums