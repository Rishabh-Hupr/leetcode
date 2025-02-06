class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/tuple-with-same-product/
            Time: O(n*2)
            Space: O(n//2) ~ O(n)
        '''
        n = len(nums)
        ans = 0
        map_ = dict()
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                if prod in map_:
                    ans += 8*map_[prod]
                    map_[prod] += 1
                else:
                    map_[prod] = 1
        return ans