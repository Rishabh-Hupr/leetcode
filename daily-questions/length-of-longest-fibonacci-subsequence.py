class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        '''
            https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
            Time: O(n^3)
            Space: O(n)
        '''
        arr_set = set(arr)
        res = 0
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                l = 2
                while nxt in arr_set:
                    cur, prev = nxt, cur
                    nxt = cur + prev
                    l += 1
                    res = max(l, res)
        return res