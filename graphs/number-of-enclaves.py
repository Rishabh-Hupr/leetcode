class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
            https://leetcode.com/problems/number-of-enclaves/
            Time: O(n*m)
            Space: O(1)
        '''
        self.n = len(grid)
        self.m = len(grid[0])
        if self.n < 3 or self.m < 3:
            return 0

        def move(i, j):
            # only process if i,j are in bounds and the node is a land
            if -1 < i < self.n and -1 < j < self.m and grid[i][j] == 1:

                # mark it processed
                grid[i][j] = -1
            
                move(i, j + 1)
                move(i, j - 1)
                move(i + 1, j)
                move(i - 1, j)

        # first and last row check
        for i in range(self.m):
            move(0, i)
            move(self.n - 1, i)
        
        # first and last col check
        for i in range(self.n):
            move(i, 0)
            move(i, self.m - 1)
        
        ans = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    ans += 1

        return ans
