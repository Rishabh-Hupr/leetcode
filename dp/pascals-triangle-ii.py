from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
            https://leetcode.com/problems/pascals-triangle-ii
            Time: O(n)
            Space: O(1)
            NOTE: comb(n, k) = n            n!
                                C    =  -----------
                                 k      k! * (n-k)!
        '''
        return [comb(rowIndex, k) for k in range(rowIndex+1)]


        '''
            Time: O(n^2)
            Space: O(1)
        '''
        # ans = [0]*(rowIndex+1)
        # ans[0] = 1
        # for i in range(1, rowIndex+1):
        #     j = 1
        #     tmp = ans[j-1]
        #     while j < i:
        #         tmp, ans[j] = ans[j],  tmp + ans[j]
        #         j += 1
        #     ans[j] = 1
        #     print(ans)
        # return ans
