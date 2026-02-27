class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
            https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
            Time: O(n * k)
            Space: O(2^k)
        '''
        ans = 2**k
        seen_set = set()
        # 00110110
        i = 1
        j = k + 1

        seen_set.add(s[:k])
        if len(seen_set) == ans:
            return True
        
        while j < len(s):
            seen_set.add(s[i:j])
            if len(seen_set) == ans:
                return True
            i += 1
            j += 1
        if i < len(s):
            seen_set.add(s[i:])

        if len(seen_set) == ans:
            return True
        return False