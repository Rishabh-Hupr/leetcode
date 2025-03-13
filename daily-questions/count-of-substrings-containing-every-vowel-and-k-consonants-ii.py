from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        '''
            aaauqeioqaaaaaqaaaieouq
            https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/
            Time: O(n)
            Space: O(1)
        '''

        ans = 0
        n = len(word)
        vwl_store = defaultdict(int)
        l = 0
        cns_cnt = vwl_cnt = 0
        for r in range(n):
            if word[r] in "aeiou":
                if vwl_store[word[r]]:
                    vwl_store[word[r]] += 1
                else:
                    vwl_store[word[r]] = 1
                    vwl_cnt += 1
            else:
                cns_cnt += 1

            while cns_cnt > k:
                # print("cns_dec", word[l], vwl_cnt, cns_cnt)
                if word[l] in "aeiou":
                    vwl_store[word[l]] -= 1
                    if vwl_store[word[l]] == 0:
                        vwl_cnt -= 1
                else:
                    cns_cnt -= 1
                l += 1

            # print("printing", l, r, cns_cnt, vwl_cnt)
            if cns_cnt == k and vwl_cnt > 4:
                tmp = r + 1
                count = 1
                while tmp < n and word[tmp] in "aeiou":
                    tmp += 1
                    count += 1
                # print(word[r], count)
                while vwl_cnt > 4 and cns_cnt == k:
                    ans += count
                    if word[l] in "aeiou":
                        vwl_store[word[l]] -= 1
                        if vwl_store[word[l]] == 0:
                            vwl_cnt -= 1
                    else:
                        cns_cnt -= 1
                    l += 1




        # for i in vowls:
        #     vwl_store[i] = 0
        
        # i = 0       # right pointer
        # cns_cnt = vwl_cnt = 0
        # while i < window:
        #     if word[i] in vwl_store:
        #         if not vwl_store[word[i]]:
        #             vwl_cnt += 1
        #         vwl_store[word[i]] += 1
        #     else:
        #         cns_cnt += 1
        #         vwl_store["cons"] += 1
        #     print(word[i], vwl_cnt, cns_cnt)
        #     i += 1
        # if vwl_cnt == 5 and vwl_cnt + cns_cnt == window:
        #     print(vwl_cnt, cns_cnt, "first here")
        #     ans += 1
        
        # j = 0        # left pointer
        # while i < n:
        #     while i < n and vwl_cnt >= 5 and cns_cnt == k:
        #         # move right
        #         if word[i] in vwl_store:
        #             if not vwl_store[word[i]]:
        #                 vwl_cnt += 1
        #             vwl_store[word[i]] += 1
        #         else:
        #             cns_cnt += 1
        #             vwl_store["cons"] += 1
        #         i += 1
        #         ans += 1
        #     while cns_cnt > k:
            
        
        return ans