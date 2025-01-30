class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            Time: O(len(s1))
            Space: O(len(s1) + len(s2))
        '''
        n = len(s2)
        m = len(s1)
        if n < m:
            return False
        
        q = Counter(s1)
        t = defaultdict(int)
        j = 0

        while j < m:
            t[s2[j]] += 1
            j += 1
        if t == q:
            return True
        i = 1
        while j < n:
            if t[s2[i - 1]] - 1:
                t[s2[i - 1]] -= 1
            else:
                t.pop(s2[i-1])
            t[s2[j]] += 1
            if t == q:
                return True
            i += 1
            j += 1
        return False    