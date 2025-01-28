class Solution:
    def searchInsert(self, arr: List[int], val: int) -> int:
        '''
            Time: O(logn)
            Space: O(1)
        '''
        if val < arr[0]:
            return 0
        elif val > arr[-1]:
            return len(arr)
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = (l+h) // 2
            if val == arr[m]:
                return m
            elif val > arr[m]:
                l = m + 1
            else:
                h = m - 1
        return l
