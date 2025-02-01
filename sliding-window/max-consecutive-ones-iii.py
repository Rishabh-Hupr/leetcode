class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        '''
            https://leetcode.com/problems/max-consecutive-ones-iii/description/
            Time: O(n + number of times zeros occur > k in a window) ~ O(n)
            Space: O(1)
        '''
        n = len(arr)
        l = zero = i = ans = 0
        r = -1
        while i < n:
            if not arr[i]:
                zero += 1
            r += 1
            while zero > k:
                if not arr[l]:
                    zero -= 1
                l += 1
            ans = max(ans, r - l + 1)
            i += 1
        return ans