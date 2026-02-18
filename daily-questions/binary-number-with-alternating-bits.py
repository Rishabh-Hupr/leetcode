class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        '''
            https://leetcode.com/problems/binary-number-with-alternating-bits/
            Time: O(logn)
            Space: O(1)
        '''
        last = n % 2
        n //= 2
        while n:
            mod = n % 2
            n //= 2
            if mod == last:
                return False
            last = mod
        return True
