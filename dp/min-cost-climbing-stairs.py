class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            https://leetcode.com/problems/min-cost-climbing-stairs/
            Time: O(n)
            Space: O(n)
        '''
        # n = len(cost)
        # arr = [0]*(n+1)
        # for i in range(2, n + 1):
        #     arr[i] = min(cost[i-1] + arr[i - 1], cost[i-2] + arr[i - 2])
        # return arr[n]

        '''
            Time: O(n)
            Space: O(1)
        '''
        n = len(cost)
        first = second = 0
        for i in range(2, n + 1):
            first, second = second, min(cost[i-1] + second, cost[i-2] + first)
        return second