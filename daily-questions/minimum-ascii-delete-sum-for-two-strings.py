class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
            Time: O(n * m) + Recursion overhead
            Space: O(n * m)
            NOTE: Recursive + memoization
        '''
        # suf1 = [0]*len(s1)
        # suf1[len(s1) - 1] = ord(s1[len(s1) - 1])
        # suf2 = [0]*len(s2)
        # suf2[len(s2) - 1] = ord(s2[len(s2) - 1])

        # for i in range(len(s1) - 2, -1, -1):
        #     suf1[i] = ord(s1[i]) + suf1[i+1]
        # for i in range(len(s2) - 2, -1, -1):
        #     suf2[i] = ord(s2[i]) + suf2[i+1]

        # memo = dict()

        # def rec(i, j):
        #     if i == len(s1):
        #         return suf2[j] if j < len(s2) else 0
        #     if j == len(s2):
        #         return suf1[i] if i < len(s1) else 0
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if s1[i] == s2[j]:
        #         memo[(i, j)] = rec(i+1, j+1)
        #     else:
        #         first = ord(s2[j]) + rec(i, j+1)
        #         second = ord(s1[i]) + rec(i+1, j)
        #         memo[(i, j)] = min(first, second)
        #     return memo[(i, j)]

        # return rec(0, 0)

        """
            Time: O(n * m) -- No recursion over head, no dict hashing
            Space: O(n * m)
        """

        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 0
        for i in range(m - 1, -1, -1):
            dp[n][i] = ord(s2[i]) + dp[n][i+1]
        for i in range(n - 1, -1, -1):
            dp[i][m] = ord(s1[i]) + dp[i+1][m]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])
        return dp[0][0]
