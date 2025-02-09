class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/count-number-of-bad-pairs/
        NOTE: LOGIC is 👇🏻
            j - i == nums[j] - nums[i]
            nums[i] - i == nums[j] - j    ------> GOOD PAIR

            Time: O(n)
            Space: O(n)
        '''
        n = len(nums)
        total = (n*(n-1)) // 2
        memo = defaultdict(int)
        for i in range(n):
            diff = nums[i] - i
            memo[diff] += 1
        for key, val in memo.items():
            if val > 1:
                total -= (val * (val - 1))//2
        return total

        '''
            Time: O(n^2)
            Space: O(1)
        '''
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j] - nums[i] != j-i:
        #             ans += 1
        # return ans