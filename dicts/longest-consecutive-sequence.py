class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Time: O(n)
            Space: O(n)
        '''
        s = set(nums)
        ans = 0
        for i in nums:
            c = 1
            if i in s:
                s.remove(i)
                if i-1 in s:
                    c += 1
                    s.remove(i-1)
                    searching_element = i - 2
                    while searching_element in s:
                        s.remove(searching_element)
                        c += 1
                        searching_element -= 1
                if i+1 in s:
                    c += 1
                    s.remove(i+1)
                    searching_element = i + 2
                    while searching_element in s:
                        s.remove(searching_element)
                        c += 1
                        searching_element += 1
            ans = max(c, ans)
        return ans

        '''
            Time: O(n)
            Space: O(n)
        '''
        # s = set(nums)
        # ans = 0
        # for i in nums:
        #     if i - 1 in s:
        #         continue
        #     else:
        #         c = 1
        #         searching_element = i + 1
        #         while searching_element in s:
        #             c += 1
        #             searching_element += 1
        #         ans = max(ans, c)
        # return ans