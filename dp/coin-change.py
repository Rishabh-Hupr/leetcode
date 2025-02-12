class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            https://leetcode.com/problems/coin-change/
            Time: O(amount*12) as number of coins <= 12
            Space: O(amount+1)
        '''
        summ = [float('inf')]*(amount+1)
        summ[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0:
                    summ[i] = min(summ[i], summ[i-j]+1)
        return summ[amount] if summ[amount]!=float('inf') else -1