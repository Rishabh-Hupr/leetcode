class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
            https://leetcode.com/problems/remove-element/description/
            Time: O(n)
            Space: O(1)
        '''
        n = len(nums) - 1
        i = c = 0
        for j in nums:
            if j != val:
                c += 1
        while i < n:
            while n > -1 and nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            i += 1
        return c