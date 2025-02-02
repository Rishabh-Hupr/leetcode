class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/remove-duplicates-from-sorted-array/
            Time: O(n)
            Space: O(unique_elements)
        '''
        # i, j = 1, 1
        # seen = set([nums[0]])
        n = len(nums)
        # while j < n:
        #     if nums[i] in seen:
        #         while j < n and nums[j] in seen:
        #             j += 1
        #         if j < n:
        #             seen.add(nums[j])
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #             j += 1
        #     else:
        #         seen.add(nums[i])
        #         i += 1
        #         j += 1
        # return i
        
        
        '''
            Time: O(n)
            Space: O(1)
        '''
        i = 1
        for j in range(1, n):
            if nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i