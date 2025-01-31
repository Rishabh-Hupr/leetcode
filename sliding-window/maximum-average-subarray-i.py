class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        '''
            Time: O(n)
            Space: (1)
        '''
        ans = float('-inf')
        tem = 0
        start = 0
        n = len(arr)
        for i in range(k):
            tem += arr[i]
        ans = max(ans, tem)
        for i in range(k, n):
            tem -= arr[start]
            tem += arr[i]
            ans = max(ans, tem)
            start += 1
        return ans / k