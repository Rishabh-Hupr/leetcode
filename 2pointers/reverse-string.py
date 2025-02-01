class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
            https://leetcode.com/problems/reverse-string/description/
            Time: O(n)
            Space: O(1)
        '''
        n = len(s)
        for i in range(n//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        