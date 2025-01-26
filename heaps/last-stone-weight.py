class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            Time: O(n) + O(nlogn) ~= O(nlogn)
            Space: O(n)
        '''
        n = len(stones)
        if n == 1:
            return stones[0]
        for i, k in enumerate(stones):
            stones[i] = -k
        heapq.heapify(stones)
        while n > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)
                n -= 1
            else:
                n -= 2
        return abs(stones[0]) if stones else 0