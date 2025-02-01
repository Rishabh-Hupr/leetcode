class Solution:
    def trap(self, arr: List[int]) -> int:
        '''
            https://leetcode.com/problems/trapping-rain-water/description/
            Time: O(n) + O(n) + O(n)
            Space: O(n) + O(n)
        '''
        n = len(arr)
        l = [0] * n
        maxl = arr[0]
        r = [0] * n
        maxr = arr[n-1]
        ans = 0
        for i in range(1, n):
            l[i] = maxl
            maxl = max(maxl, arr[i])
        
        for i in range(n-2, -1, -1):
            r[i] = maxr
            maxr = max(maxr, arr[i])
        
        for i in range(n):
            if min(l[i], r[i]) > arr[i]:
                ans += min(l[i], r[i]) - arr[i]
        return ans