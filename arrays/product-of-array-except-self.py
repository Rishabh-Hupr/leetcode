class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # '''
        #     https://leetcode.com/problems/product-of-array-except-self/description/
        #     Time: O(n)
        #     Space: O(1)
        # '''
        # n = len(nums)
        # ans = [1]*n
        # fix = 1
        # for i in range(1, n):
        #     ans[i] = fix * nums[i-1]
        #     fix = ans[i]
        # fix = 1
        # for i in range(n-2, -1, -1):
        #     fix = fix * nums[i+1]
        #     ans[i] = ans[i] * fix

        # return ans

        '''
            Time: O(n)
            Space: O(1)
        '''
        n = len(nums)
        ans = [1 for _ in range(n)]

        for i in range(n-2, -1, -1):
            ans[i] = ans[i+1] * nums[i+1] 
        
        tmp = 1
        for i in range(n-1):
            ans[i] = tmp * ans[i]
            tmp *= nums[i]
        ans[n-1] = tmp
        return ans
