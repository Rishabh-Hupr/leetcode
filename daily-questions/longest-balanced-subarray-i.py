class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/longest-balanced-subarray-i/
            Time: O(n^2)
            Space: O(n)

            NOTE: The prefix-difference approach fails because knowing the counts from the start doesn’t tell you the exact distinct numbers in a subarray — two prefixes can have the same difference,
            but the elements between them may differ. We switch to O(n^2) to track the actual distinct even and odd numbers in each subarray, ensuring correctness.
        '''

        n = len(nums)
        ans = 0
        for i in range(n):
            dEven = 0
            dOdd = 0
            store = set()
            for j in range(i, n):
                if nums[j] not in store:
                    if nums[j] % 2:
                        dOdd += 1
                    else:
                        dEven += 1
                    store.add(nums[j])
                if dOdd == dEven:
                    ans = max(ans, j - i + 1)
            del store

        
        return ans