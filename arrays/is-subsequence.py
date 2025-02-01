class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
            https://leetcode.com/problems/is-subsequence/description/
            Time: O(n)
            Space: O(1)
        '''
        i = 0
        n = len(s)
        for j in t:
            if i < n and s[i] == j:
                i += 1
        if i == n:
            return True
        return False
