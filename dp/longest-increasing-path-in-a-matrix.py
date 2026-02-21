class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
            The idea is to use a depth first search to calculate the longest increasing path for each cell in the matrix.
            We will keep track of the longest path we have seen so far and update it whenever we
            find a new maximum. We will also use a cache to store the longest path for each cell to avoid redundant calculations.

            https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
            Time: O(m*n) where m is the number of rows and n is the number of columns in the matrix, since we visit each cell once.
            Space: O(m*n) in the worst case, since we use a cache that can store the longest path for each cell in the matrix.
        '''
		self.m, self.n = len(matrix), len(matrix[0])
		ans = float('-inf')
		self.cache = dict()
		self.TOP = "T"
		self.BOTTOM = "B"
		self.LEFT = "L"
		self.RIGHT = "R"
		self.SOURCE = "S"

		def move(i, j, incomingDirection):
			if (i, j) in self.cache:
				return self.cache[(i, j)]
			curVal = matrix[i][j]
			up, down, left, right = 0, 0, 0, 0

			if incomingDirection == self.SOURCE:
				if j + 1 < self.n and matrix[i][j+1] > curVal:
					right = move(i, j + 1, "R") # right
				if j - 1 > -1 and matrix[i][j-1] > curVal:
					left = move(i, j - 1, "L") # left
				if i + 1 < self.m and matrix[i+1][j] > curVal:
					down = move(i + 1, j, "D") # down
				if i - 1 > -1 and matrix[i-1][j] > curVal:
					up = move(i - 1, j, "U") # up
			else:

				if incomingDirection != self.LEFT:
					if j + 1 < self.n and matrix[i][j+1] > curVal:
						right = move(i, j + 1, "R") # right
			
				if incomingDirection != self.RIGHT:
					if j - 1 > -1 and matrix[i][j-1] > curVal:
						left = move(i, j - 1, "L") # left

				if incomingDirection != self.TOP:
					if i + 1 < self.m and matrix[i+1][j] > curVal:
						down = move(i + 1, j, "D") # down
	
				if incomingDirection != self.BOTTOM:
					if i - 1 > -1 and matrix[i-1][j] > curVal:
						up = move(i - 1, j, "U") # up

			self.cache[(i, j)] = 1 + max(up, down, right, left)
			return self.cache[(i, j)]
			


		for i in range(self.m):
			for j in range(self.n):
				ans = max(ans, move(i, j, "S"))
		return ans
			