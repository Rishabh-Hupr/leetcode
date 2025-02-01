class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
            https://leetcode.com/problems/minimum-window-substring/description/
            Time: O(n + m)
            Space: O(m)
            NOTE: FORGET THE COMMENTED CODE, THAT'S WRONG
        '''
        n = len(s)
        m = len(t)
        if m > n or not m or not n:
            return ""
        cT = Counter(t)
        # cS = dict()
        # winStart = [-1, False]
        # j = 0
        # tup = [0, j]
        # min_win  = 10**5 + 1
        # for i in range(n):
        #     if s[j] in cT:
        #         if not winStart[1]:
        #             winStart[0] = i
        #             winStart[1] = True
        #         cS[s[j]] += 1
        #         while cS[s[j]] > cT[s[j]] or s[winStart[0]] not in cT:
        #             if s[winStart[0]] == s[j]:
        #                 cS[s[j]] -= 1
        #             elif s[winStart[0]] in cS:
        #                 cS[s[winStart[0]]] -= 1
        #                 if not cS[s[winStart[0]]]:
        #                     cS.pop(s[winStart[0]])
        #             winStart[0] += 1
        #     if cS == cT:
        #         if j - winStart[0] + 1 < min_win:
        #             min_win = j - winStart[0] + 1
        #             tup[0] = winStart[0]
        #             tup[1] = j

        #         # while winStart[0] < n and cS == cT:
        #         cS[s[winStart[0]]] -= 1
        #         if not cS[s[winStart[0]]]:
        #             cS.pop(s[winStart[0]])
        #         winStart[0] += 1
        #         while winStart[0] < n and s[winStart[0]] not in cT:
        #             winStart[0] += 1
        #     j += 1
        
        # return s[tup[0]:tup[1]+1] if winStart[1] else ""
        winStart = [-1, False]
        cnt = 0
        start = -1
        i = 0
        min_win  = 10**5 + 1
        while i < n:
            if s[i] in cT:
                if not winStart[1]:
                    winStart[0] = i
                    winStart[1] = True
                if cT[s[i]] > 0:
                    cnt += 1

                cT[s[i]] -= 1
                # if s[i] not in cS:
                #     nS += 1
                #     cS[s[i]] = 1
                # else:
                #     cS[s[i]] += 1
            while cnt == m:
                if i - winStart[0] + 1 < min_win:
                    min_win = i - winStart[0] + 1
                    start = winStart[0]
                if s[winStart[0]] in cT:
                    cT[s[winStart[0]]] += 1
                    if cT[s[winStart[0]]] > 0:
                        cnt -= 1
                # if s[winStart[0]] in cS:
                #     if cS[s[winStart[0]]] == 1:
                #         cS.pop(s[winStart[0]])
                #         nS -= 1
                #     else:
                #         cS[s[winStart[0]]] -= 1
                    # if winStart[0] < i and (s[winStart[0]] in cT and cS[s[winStart[0]]] > cT[s[winStart[0]]]):
                    #     if cS[s[winStart[0]]] > cT[s[winStart[0]]]:
                    #         cS[s[winStart[0]]] -= 1
                winStart[0] += 1

            i += 1
        return s[start:start + min_win] if min_win != 10**5 + 1 else ""