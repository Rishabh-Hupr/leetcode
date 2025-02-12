class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
            max-sum-of-a-pair-with-equal-sum-of-digits
            https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
            NOTE: There are multiple solutions listed here, you can check which ever you like
        '''
        def digit_sum(num):
            ans = 0
            while num:
                ans += (num%10)
                num //= 10
            return ans
        n = len(nums)
        ans = -1
        '''
            Time: O(nlogn)
            Space: O(n)
        '''
        # tmp = []
        # for i in range(n):
        #     tmp.append(tuple([digit_sum(nums[i]), nums[i]]))
        # tmp.sort()
        # i = 0
        # for j in range(1, n):
        #     if tmp[i][0] == tmp[j][0]:
        #         ans = max(ans, tmp[i][1] + tmp[j][1])
        #     i += 1
            
        # return ans

        '''
            Time: O(n*9)
            Space: O(n)
        '''
        # memo = defaultdict(list)
        # for i in range(n):
        #     x = digit_sum(nums[i])
        #     if x in memo:
        #         memo[x][0] = max(memo[x][0], memo[x][1] + nums[i])
        #         memo[x][1] = max(memo[x][1], nums[i])
        #         ans = max(ans, memo[x][0])
        #     else:
        #         memo[x] = [x, nums[i]]
        # return ans

        '''
            Time: O(n + 9*n)
            Space: O(n)
        '''
        summ = []
        for i in range(n):
            summ.append(digit_sum(nums[i]))
        memo = defaultdict(list)
        for i in range(n):
            x = summ[i]
            if x in memo:
                memo[x][0] = max(memo[x][0], memo[x][1] + nums[i])
                memo[x][1] = max(memo[x][1], nums[i])
                ans = max(ans, memo[x][0])
            else:
                memo[x] = [nums[i], nums[i]]

        return ans
