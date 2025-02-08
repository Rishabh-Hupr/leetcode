class Solution:
    def romanToInt(self, s: str) -> int:
        '''
            https://leetcode.com/problems/roman-to-integer/
            Time: O(n)
            Space: O(1)
        '''
        n = len(s)
        i = ans = 0
        dct = {"I": 1, "X": 10, "C": 100, "V": 5, "L": 50, "D": 500, "M": 1000}
        while i < n-1:
            if s[i] == "I":
                if s[i+1]  == "V":
                    ans += 4
                    i += 2
                elif s[i+1] == "X":
                    ans += 9
                    i += 2
                else:
                    ans += 1
                    i += 1
            elif s[i] == "X":
                if s[i+1]  == "L":
                    ans += 40
                    i += 2
                elif s[i+1] == "C":
                    ans += 90
                    i += 2
                else:
                    ans += 10
                    i += 1
            elif s[i] == "C":
                if s[i+1]  == "D":
                    ans += 400
                    i += 2
                elif s[i+1] == "M":
                    ans += 900
                    i += 2
                else:
                    ans += 100
                    i += 1
            else:
                ans += dct[s[i]]
                i += 1
        if i < n:
            ans += dct[s[i]]
        return ans
