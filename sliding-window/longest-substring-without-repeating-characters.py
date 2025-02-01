class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        '''
            https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
            Time: O(n + number of times duplicates occur in sequence) ~ O(n)
            Space: O(unique_elements)
        '''
        l = 0
        r = -1
        data = set()
        maxi = 0
        for i in arr:
            if i in data:
                while i != arr[l]:
                    data.remove(arr[l])
                    l += 1
                l += 1
            else:
                data.add(i)
            r += 1
            maxi = max(maxi, r - l + 1)
        return maxi