class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            https://leetcode.com/problems/3sum/
            Time: O(nlogn) + O(n^2) ~~ O(n^2)
            Space: O(1), since we have inplace sorting and only store the answer
        '''
        nums.sort()
        # -4 -1 -1 0 1 2
        
        ans = []
        n = len(nums)
        for i in range(n):
            fst = nums[i]

            # only positive numbers left in the array
            if fst > 0:
                return ans
            if i > 0 and fst == nums[i-1]:
                i += 1
                continue
            
            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = fst + nums[lo] + nums[hi]
                if summ == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < n and nums[lo] == nums[lo - 1]:
                        lo += 1
                    hi -= 1
                    while hi > -1 and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif summ > 0:
                    hi -= 1
                else:
                    lo += 1
        return ans
