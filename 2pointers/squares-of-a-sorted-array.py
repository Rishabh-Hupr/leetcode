class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        '''
            https://leetcode.com/problems/squares-of-a-sorted-array/description/
            Time: O(n) + O(n)
            Space: O(n)
        '''
        # ans = list()
        # n = len(arr)
        # small = 0
        # for i in arr:
        #     if i < 0:
        #         small += 1
        #     else:
        #         break
        # i = small - 1
        # j = small
        # while i > -1 and j < n:
        #     if abs(arr[i]) < arr[j]:
        #         ans.append(arr[i]**2)
        #         i -= 1
        #     else:
        #         ans.append(arr[j]**2)
        #         j += 1
        # while j < n:
        #     ans.append(arr[j]**2)
        #     j += 1
        # while i > -1:
        #     ans.append(arr[i]**2)
        #     i -= 1
        # return ans

        '''
            Time: O(n)
            Space: O(n)
        '''
        n = len(arr)
        ans = [0]*n
        i, j = 0, n-1
        c = -1
        while i <= j:
            if abs(arr[i]) > abs(arr[j]):
                ans[c] = arr[i]**2
                i += 1
            else:
                ans[c] = arr[j]**2
                j -= 1
            c -= 1
        return ans