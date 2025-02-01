class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
            foo bar
            f -> b
            o -> a          FALSE

            foo aab

            f -> a
            o -> b
            abb             FALSE

            So order matters along with frequency
        '''
        # count_s = Counter(s)
        # count_t = Counter(t)

        # j = 0
        # for i in s:
        #     if count_s[i] != count_t[t[j]]:
        #         return False
        #     count_s[i] -= 1
        #     count_t[t[j]] -= 1

        #     j += 1
        # return True

        '''
            https://leetcode.com/problems/isomorphic-strings/description/
            Time: O(n)
            Space: O(n)
        '''
        store1 = dict()
        store2 = dict()
        j = 0
        for i in s:
            if i in store1:
                if t[j] != store1[i]:
                    return False
            elif t[j] in store2:
                if i != store2[t[j]]:
                    return False
            else:
                store1[i] = t[j]
                store2[t[j]] = i

            j += 1
        return True