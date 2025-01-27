class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        '''
            Time: O(n)
            Space: O(1)
        '''
        ans = 0
        sml = arr[0]
        for i in arr:
            if i - sml > 0:
                ans += (i - sml)
                sml = i
            sml = min(i, sml)
        return ans


        '''
            Same
        '''
        # ans = 0
        # sml = arr[0]
        # for i in arr:
        #     if i - sml > ans:
        #         ans += (i - sml)
        #     sml = i
        # return ans