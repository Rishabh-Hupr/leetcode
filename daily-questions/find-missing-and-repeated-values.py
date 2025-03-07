class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        '''
            https://leetcode.com/problems/find-missing-and-repeated-values/description/
            Time: O(n^2)
            Space: O(n^2)
        '''
        seen = set()
        ans = []
        run_sum = 0
        n = len(grid)**2
        should_be_sum = n * (n + 1) // 2
        for item in grid:
            for elem in item:
                if elem in seen:
                    ans.append(elem)
                else:
                    seen.add(elem)
                    run_sum += elem
        ans.append(should_be_sum - run_sum)
        return ans