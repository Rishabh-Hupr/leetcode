class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
            Time: O((n-k)*k)
            Space: O(k)
        '''
        # s = set()
        # n = len(nums)
        # if k >= n:
        #     k = n - 1
        # ini = 0
        # for i in range(k+1):
        #     s.add(nums[i])
        # if len(s) != k+1:
        #     return True
        # for i in range(k+1, n):
        #     s.remove(nums[ini])
        #     s.add(nums[i])
        #     if len(s) != k+1:
        #         return True
        #     ini += 1
        # return False


        '''
            Time: O(n)
            Space: O(n)
        '''
        store = dict()
        for i, val in enumerate(nums):
            if val in store:
                if i - store[val] <= k:
                    return True
                store[val] = i
            else:
                store[val] = i
        return False
