class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
            Time: O(n*m)
            Space: O(1)
        '''
        n, m = len(mat), len(mat[0])
        row, col = False, False
        for i in range(n):
            if mat[i][0] == 0:
                col = True
        for j in range(m):
            if mat[0][j] == 0:
                row = True

        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    mat[0][j] = mat[i][0] = 0

        for i in range(n-1, 0, -1):
            for j in range(m-1, 0, -1):
                if not mat[i][0] or not mat[0][j]:
                    mat[i][j] = 0
        
        if col:
            for i in range(n):
                if mat[0][0] == 0:
                    mat[i][0] = 0
        
        if row:
            for j in range(m):
                if mat[0][0] == 0:
                    mat[0][j] = 0