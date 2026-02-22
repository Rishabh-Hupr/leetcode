class Solution:
    def binaryGap(self, n: int) -> int:
        '''
            https://leetcode.com/problems/binary-gap/
            Time: O(len(str(binary_representation(n))))
            Space: O(len(str(binary_representation(n))))

        '''
        s = bin(n)[2:]
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == "0":
                j += 1
            if j < n and s[j] == "1":
                ans = max(ans, j - i) 
            i = j
        return ans
