class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            https://leetcode.com/problems/group-anagrams/description/
            Time: O(n*avg_length_of_each_string) in worst case i.e. O(n*100) as n <= 100
            Space: O(n)
        '''
        mapp = defaultdict(list)
        for i in strs:
            s = [0]*26
            for j in i:
                s[ord(j) - 97] += 1
            mapp[tuple(s)].append(i)
        ans = list()
        for i in mapp:
            ans.append(mapp[i])
        return ans

        '''
            Time: O(n*klogk) where k = avg_length_of_each_string
            Space: O(n)
        '''
        # mapp = defaultdict(list)
        # for i in strs:
        #     s = ''.join(sorted(i))
        #     mapp[s].append(i)

        # return list(mapp.values())
