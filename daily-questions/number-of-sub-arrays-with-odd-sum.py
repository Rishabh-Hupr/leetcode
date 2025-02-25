class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
            https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum
            Time: O(n)
            Space: O(1)
        '''
        cur_sum = 0
        ans = 0
        n_even = n_odd = 0
        for i in arr:
            cur_sum += i
            if cur_sum % 2:
                ans += 1 + n_even
                n_odd += 1
            else:
                ans += n_odd
                n_even += 1
        return ans % (10**9+7)
