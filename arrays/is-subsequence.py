class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        for j in t:
            if i < n and s[i] == j:
                i += 1
        if i == n:
            return True
        return False
