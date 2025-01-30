class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
            Time: O(len(s))
            Space: O(1) ~ O(2 * 26)
        '''
        # chrS = [0]*26
        # chrP = [0]*26
        # m = 0
        # for i in p:
        #     m += 1
        #     chrP[ord(i) - 97] += 1
        # j = 0
        # while j < len(s) and j < m:
        #     chrS[ord(s[j]) - 97] += 1
        #     j += 1
        # ans = list()
        # if chrS == chrP:
        #     ans.append(0)
        # i = 1
        # while j < len(s):
        #     chrS[ord(s[i - 1]) - 97] -= 1
        #     chrS[ord(s[j]) - 97] += 1
        #     if chrS == chrP:
        #         ans.append(i)
        #     i += 1
        #     j += 1
        # return ans

        '''
            Time: O(n)
            Space: O(1)
        '''
        q = Counter(p)
        t = defaultdict(int)

        j = 0
        m = len(p)
        n = len(s)
        if m > n:
            return []
        while j < m:
            t[s[j]] += 1
            j += 1
        ans = list()
        if t == q:
            ans.append(0)
        i = 1
        while j < len(s):
            if t[s[i - 1]] - 1:
                t[s[i - 1]] -= 1
            else:
                t.pop(s[i-1])
            t[s[j]] += 1
            if t == q:
                ans.append(i)
            i += 1
            j += 1
        return ans