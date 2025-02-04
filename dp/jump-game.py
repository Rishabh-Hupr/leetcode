class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            https://leetcode.com/problems/jump-game/
            Time: O(n)
            Space: O(1)
        '''
        maxi = nums[0]
        n = len(nums)
        for i in range(1, n):
            if maxi - i > -1:
                if maxi - i:
                    maxi = max(maxi, nums[i] + i)
                else:
                    maxi = nums[i] + i
            else:
                return False
        return True