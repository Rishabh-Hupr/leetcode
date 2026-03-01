class Solution:
    def pacificAtlantic(self, arr: List[List[int]]) -> List[List[int]]:
        '''
            https://leetcode.com/problems/pacific-atlantic-water-flow/
            Time: O(n*m)
            Space: O(n*m)

            NOTE: Trick is to start form the border nodes again, as in check fro all the nodes that can reach the pacific
            and then check for all the nodes that ®each the atlnatic and then take the intersection of the two sets.
            This way we can avoid doing a dfs/bfs for every node in the matrix and just do it for the border nodes.
        '''

        n = len(arr)
        m = len(arr[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def validityCheck(i, j, val):
            if -1 < i < n and -1 < j < m and arr[i][j] >= val and (i, j) not in vis:
                return True

        def dfs(i, j):
            for dx, dy in dirs:
                newX, newY = i + dx, j + dy
                if validityCheck(newX, newY, arr[i][j]):
                    vis.add((newX, newY))
                    dfs(newX, newY)

        
        vis = set()
        # first row and first column check for pacific border check
        for i in range(m):
            vis.add((0, i))
            dfs(0, i)
        for i in range(n):
            vis.add((i, 0))
            dfs(i, 0)
        pacific = vis
        
        vis = set()
        # last row and last column check for atlantic border check
        for i in range(m):
            vis.add((n - 1, i))
            dfs(n - 1, i)
        for i in range(n):
            vis.add((i, m - 1))
            dfs(i, m - 1)
        atlantic = vis
        
        return list(pacific & atlantic)
        