from collections import deque as dq

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
            https://leetcode.com/problems/jump-game-ii/
            Time: O(n)
            Space: O(n)
        '''
        # to reach index 0, we need 0 steps
        # to reach index 1, we would need if nums[0] + 0 >= 1
        # to reach index 2, we would need if nums[1]

        # 2 3 1 1 4
        #   1 1

        # ans = [0, 1, 1, 2, 2]
        n = len(nums)
        if n == 1:
            return 0
        
        queue = dq()
        queue.append(0)
        nums[0] = (nums[0], 0)
        
        for i in range(1, n):
            val = nums[i]
            # if we can't reach i from the last biggest jump
            while nums[queue[0]][0] + queue[0] < i:
                queue.popleft()
            
            # now that we are sure that we can reach to i from a valid jump
            nums[i] = (val, 1 + nums[queue[0]][1])
            
            # if our current jump is going to land us shorter than the last biggest jump, then we don't append it in the queue
            if val + i > nums[queue[0]][0] + queue[0]:
                queue.append(i)
        return nums[-1][1]


OR

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
            Time: O(n)
            Space: O(1)
        '''
        n = len(nums)
        if n == 1:
            return 0
        
        curr = nums[0]
        tmp_far = nums[0]
        ans = 1
        
        for i in range(1, n):
            # if over my so far current biggest jump(curr), then need to another jump, also update my so far current biggest jump(curr) to tmp_far
            if i > curr:
                ans += 1
                curr = tmp_far

            # calculate any possible biggest jump(tmp_far) while checking my so far current biggest found(curr)
            tmp_far = max(tmp_far, nums[i] + i)

        
        return ans
