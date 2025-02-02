class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        '''
            https://leetcode.com/problems/find-indices-with-index-and-value-difference-i
            Time: O(n2)
            Space: O(1)
        '''
        n = len(nums)
        for i in range(n):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]