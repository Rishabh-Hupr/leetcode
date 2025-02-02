class Solution:
    def fib(self, n: int) -> int:
        '''
            https://leetcode.com/problems/fibonacci-number/
            Time: O(n)
            Space: O(1)
        '''
        if n == 0:
            return 0
        elif n == 1:
            return 1
        second_last, last = 0, 1
        for i in range(2, n + 1):
            second_last, last = last, second_last + last
        return last