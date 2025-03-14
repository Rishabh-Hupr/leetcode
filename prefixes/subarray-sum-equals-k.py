class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            https://leetcode.com/problems/subarray-sum-equals-k/description/

            Time: O(n)
            Space: O(n)
        '''
        cur = 0
        store = { 0 : 1 }
        ans = 0
        for i in nums:
            cur += i
            ans += store.get(cur - k, 0)
            store[cur] = 1 + store.get(cur, 0)
        return ans