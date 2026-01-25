class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
            Time: O(n)
            Space: O(1)
        '''
        ini_x = points[0][0]
        ini_y = points[0][1]
        ans = 0

        for x, y in points:
            ans += max(abs(x - ini_x), abs(y - ini_y))
            ini_x, ini_y = x, y
        return ans
