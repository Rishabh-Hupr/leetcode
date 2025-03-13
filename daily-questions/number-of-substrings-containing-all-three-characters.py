from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
            https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
            Time: O(n)
            Space: O(1)
        '''
        l, r = 0, 0
        n = len(s)
        store = defaultdict(int)
        run_cnt = 0
        ans = 0
        while r < n:
            if not store[s[r]]:
                run_cnt += 1
            store[s[r]] += 1
            while run_cnt == 3:
                ans += (n - r)
                store[s[l]] -= 1
                if not store[s[l]]:
                    run_cnt -= 1
                l += 1
            r += 1
        return ans