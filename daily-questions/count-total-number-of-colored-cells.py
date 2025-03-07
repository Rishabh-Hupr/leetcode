class Solution:
    def coloredCells(self, n: int) -> int:
        '''
            https://leetcode.com/problems/count-total-number-of-colored-cells/
            Time: O(n)
            Space: O(1)
        '''
        # ans = 1
        # for i in range(n):
        #     ans += (i*4)
        # return ans

        '''
            Time: O(1)
            Space: O(1)
        '''
        return 2*n*(n-1)+1