class Solution:
	def isDigitorialPermutation(self, n: int) -> bool:
        '''
            https://leetcode.com/problems/check-digitorial-permutation/
            Time: O(len(str(n))), max is 9
            Space: O(1), max we will store is 9 elements in store and arr
        '''
		self.maxx = 0
		
		def getDigits(n):
			arr = []
			while n:
				digit = n % 10
				arr.append(digit)
				self.maxx = max(self.maxx, digit)
				n //= 10
			return arr
			
		
		store = {0: 1}
		def factorial(n):
			if n:
				store[n] = n * factorial(n-1)
			return store[n]
		
		arr = getDigits(n)
		factorial(self.maxx)
		summ = sum([store[val] for val in arr])
		return sorted([str(i) for i in arr]) == sorted(str(summ))