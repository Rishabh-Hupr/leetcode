class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            https://leetcode.com/problems/climbing-stairs/
            Time: O(n)
            Space: O(1)
        '''
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            first, second = second, first + second
        return second