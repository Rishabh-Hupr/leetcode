class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        '''
            https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/?envType=daily-question&envId=2025-02-05
            Time: O(n)
            Space: O(1)
        '''
        c = 0
        index = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                index.append(i)
                c += 1
            if c > 2:
                return False
        if not c:
            return True
        elif c == 2:
            if s1[index[0]] == s2[index[1]] and s1[index[1]] == s2[index[0]]:
                return True
        return False