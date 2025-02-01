class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        '''
            https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
            Time: O(n)
            Space: O(1)
        '''
        i, j = 0, len(arr) - 1
        while i < j:
            x = arr[i] + arr[j]
            if x > target:
                j -= 1
            elif x < target:
                i += 1
            else:
                return [i+1, j+1] 