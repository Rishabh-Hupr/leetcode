class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            https://leetcode.com/problems/subsets/
            Time: O(2^n)
            Space: O(logn + n) ~ O(n)
        '''
        ans = [[]]
        n = len(nums)
        stk = []
        def rec(i):
            nonlocal n
            if i >= n:
                return
            rec(i+1)
            stk.append(nums[i])
            rec(i+1)
            ans.append(stk[:])
            stk.pop()
        rec(0)
        return ans
