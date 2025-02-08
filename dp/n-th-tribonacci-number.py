class Solution:
    def tribonacci(self, n: int) -> int:
        '''
            https://leetcode.com/problems/n-th-tribonacci-number
            Time: O(n)
            Space: O(1)
        '''
        if n == 0:
            return 0
        f, s, t = 0, 1, 1
        for i in range(3, n + 1):
            f, s, t = s, t, f + s + t
        return t