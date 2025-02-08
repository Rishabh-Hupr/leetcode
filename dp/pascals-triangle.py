class Solution:
    # Return 2d array consisting of the pascal's triangle for given 'n'
    def generate(self, n: int):
        '''
            https://leetcode.com/problems/pascals-triangle/
            Time: O(n*n)
            Space: O(1)
        '''
        ans = [[] for i in range(n)]
        ans[0].append(1)
        for i in range(1, n):
            ans[i].append(1)
            for j in range(i - 1):
            ans[i].append(ans[i-1][j] + ans[i-1][j+1])
            ans[i].append(1)
        return ans

