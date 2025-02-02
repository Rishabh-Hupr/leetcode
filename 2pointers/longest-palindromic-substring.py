class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
            https://leetcode.com/problems/longest-palindromic-substring/description/
            Time: O(n*2)
            Space: O(1)
        '''
        n = len(s)
        st = 0
        maxi  = 1
        for elem in range(n):
            i, j = elem - 1, elem + 1
            while i > -1 and j < n and s[i] == s[j]:
                if j - i + 1 > maxi:
                    st = i
                    maxi = j - i + 1
                i -= 1
                j += 1
            i, j = elem - 1, elem
            while i > -1 and j < n and s[i] == s[j]:
                if j - i + 1 > maxi:
                    st = i
                    maxi = j - i + 1
                i -= 1
                j += 1
        return s[st: st + maxi]