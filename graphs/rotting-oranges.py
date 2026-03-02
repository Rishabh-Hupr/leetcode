class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            https://leetcode.com/problems/rotting-oranges/
            Time: O(n * m)
            Space: O(n * m)

            NOTE: Track all rotten organges first so and then start a BFS for all of to check all the fresh oranges using a queue
            until either the grid is exhausted or there are no more oanges left. If there are no more fresh oranges left then return the time taken else return -1.
        '''
        n = len(grid)
        m = len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def validityCheck(i, j):
            if -1 < i < n and -1 < j < m and grid[i][j] == 1:
                return True

        def bfs(rotQue, freshCount):
            # time to rot all possible oranges from cur orange
            mins = 0
            while rotQue and freshCount:
                levelSize = len(rotQue)

                for _ in range(levelSize):
                    i, j = rotQue.popleft()

                    # neighbour check
                    for di, dj in dirs:
                        newI, newJ = i + di, j + dj
                        if validityCheck(newI, newJ):
                            freshCount -= 1
                            rotQue.append((newI, newJ))
                            grid[newI][newJ] = 2
                mins += 1
            
            return mins, not bool(freshCount)

        ans = -1

        freshOranges = 0
        rotQue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    rotQue.append((i, j))
        
        if freshOranges == 0:
            return 0
        
        ans, possible = bfs(rotQue, freshOranges)
        if possible:
            return ans
        return -1
