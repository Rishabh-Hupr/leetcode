class Solution:
    def numSteps(self, s: str) -> int:
        '''
            https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
            Time: O(n)
            Space: O(1)
        '''
        num = int(s, 2)
        ans = 0
        while num != 1:
            if num % 2:
                num += 1
            else:
                num >>= 1
            ans += 1
        return ans