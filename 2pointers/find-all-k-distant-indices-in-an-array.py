class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        '''
            https://leetcode.com/problems/find-indices-with-index-and-value-difference-i
            Time: O(n2)
            Space: O(n)
        '''
        ans = set()
        n = len(nums)
        for i, val in enumerate(nums):
            if val == key:
                j = i - 1
                while j > -1 and j >= i - k:
                    ans.add(j)
                    j -= 1
                j = i
                while j < n and j <= i + k:
                    ans.add(j)
                    j += 1
        return list(ans)