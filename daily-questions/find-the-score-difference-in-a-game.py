class Solution:
	def scoreDifference(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/find-the-score-difference-in-a-game/
            Time: O(n)
            Space: O(1)
        '''
		active = True
		scoreDifference = 0

		for i, val in enumerate(nums):
			if val % 2:
				active = not active
			# applying sequentially
			if i % 6 == 5:
				active = not active
			if active:
				scoreDifference += val
			else:
				scoreDifference -= val
		return scoreDifference
