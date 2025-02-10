class Solution:
    def clearDigits(self, s: str) -> str:
        '''
            https://leetcode.com/problems/clear-digits/
            Time: O(n)
            Space: O(n)
        '''
        stk = []
        for i in s:
            if i.isnumeric():
                if stk:
                    stk.pop()
            else:
                stk.append(i)
        return ''.join(stk)