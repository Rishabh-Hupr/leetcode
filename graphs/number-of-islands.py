class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            https://leetcode.com/problems/number-of-islands/
            Time: O(m*n*(number_of_unique_islands))
            Space: O(m*n) --- without using seen set()
        '''
        m, n = len(grid), len(grid[0])
        # seen = set()

        # defining dfs for the grid
        # def dfs(i, j):
        #     if len(grid) <= i or i < 0 or j >= len(grid[0]) or j < 0:
        #         return
        #     if (i, j) in seen:
        #         return
        #     if int(grid[i][j]):
        #         seen.add((i, j))
        #         dfs(i-1, j)
        #         dfs(i, j+1)
        #         dfs(i+1, j)
        #         dfs(i, j-1)

        stk = []
        ans = 0
        for i in range(m):
            for j in range(n):
                if int(grid[i][j]):
                    #  and (i, j) not in seen:
                    stk = []
                    stk.append((i, j))
                    # seen.add((i, j))
                    while stk:
                        x, y = stk.pop()
                        if m <= x or x < 0 or y >= n or y < 0:
                            continue
                        if int(grid[x][y]):
                            grid[x][y] = "0"
                            # if (x-1, y) not in seen:
                            stk.append((x-1, y))
                                # seen.add((x-1, y))
                            # if (x, y+1) not in seen:
                            stk.append((x, y+1))
                                # seen.add((x, y+1))
                            # if (x+1, y) not in seen:
                            stk.append((x+1, y))
                                # seen.add((x+1, y))
                            # if (x, y-1) not in seen:
                            stk.append((x, y-1))
                                # seen.add((x, y-1))
                    ans += 1
                    # dfs(i, j)
        return ans