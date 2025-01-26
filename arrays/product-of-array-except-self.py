class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Time: O(n)
            Space: O(1)
        '''
        n = len(nums)
        ans = [1]*n
        fix = 1
        for i in range(1, n):
            ans[i] = fix * nums[i-1]
            fix = ans[i]
        fix = 1
        for i in range(n-2, -1, -1):
            fix = fix * nums[i+1]
            ans[i] = ans[i] * fix

        return ans
