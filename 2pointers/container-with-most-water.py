class Solution:
    def maxArea(self, arr: List[int]) -> int:
        '''
            https://leetcode.com/problems/container-with-most-water/description/
            Time: O(n)
            Space: O(1)
        '''
        n = len(arr)
        i = 0
        j = n - 1
        maxi = 0
        while i < j:
            x = (j-i) * min(arr[i], arr[j])
            maxi  = max(x, maxi)
            if arr[i] < arr[j]:
                i += 1
            else:
                j -= 1
        return maxi