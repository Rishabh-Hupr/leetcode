class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/majority-element/description/
            ### Boyer-Moore Voting Algorithm ###
            Time: O(n)
            Space: O(1)
        '''
        can = None
        c = 0
        for i in nums:
            if c == 0:
                can = i
            c += 1 if can == i else -1
        
        return can
        '''
            Time: O(n)
            Space: O(n)
        '''
        # store = defaultdict(int)
        # n = len(nums)
        # for i in nums:
        #     store[i] += 1
        #     if store[i] > n // 2:
        #         return i
