class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            https://leetcode.com/problems/permutations/
            Time: O(n * n!)
            Space: O(n)
        '''
        ans = []
        tmp = []
        def dfs():
            if len(tmp) == len(nums):
                ans.append(tmp[:])
                return

            for i in range(len(nums)):
                if nums[i] != 11:
                    t = nums[i]
                    nums[i] = 11
                    tmp.append(t)
                    dfs()

                    nums[i] = t
                    tmp.pop()

        dfs()
        return ans
            