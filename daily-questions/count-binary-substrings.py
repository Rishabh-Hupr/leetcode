class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
            https://leetcode.com/problems/count-binary-substrings/
            Time: O(n)
            Space: O(1)
        '''
        prev = 0
        curr = 1
        i = 1
        n = len(s)
        ans = 0
        
        while i < n:
            if s[i] == s[i-1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1
            i += 1
        ans += min(curr, prev)
        return ans
