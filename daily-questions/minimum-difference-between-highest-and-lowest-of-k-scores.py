class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
            Time: O(nlogn + n)
            Space: O(1)
        '''
        if k == 1:
            return 0
        nums.sort()
        i = 0
        j = k - 1
        ans = 10**5 + 1
        while j < len(nums):
            ans = min(ans, nums[j] - nums[i])
            j += 1
            i += 1
        
        return ans