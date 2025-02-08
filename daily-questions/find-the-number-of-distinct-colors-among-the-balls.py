class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        '''
            https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
            Time: O(n), where n = number of queries
            Space: O(m), where m = limit + 1
        '''
        balls = dict()
        colors = defaultdict(int)
        c = 0
        ans = list()
        for qry in queries:
            if qry[0] in balls:
                if colors[balls[qry[0]]] == 1:
                    colors.pop(balls[qry[0]])
                    c -= 1
                    if qry[1] not in colors:
                        c += 1
                else:
                    if qry[1] not in colors:
                        c += 1
                    colors[balls[qry[0]]] -= 1
            elif qry[1] not in colors:
                c += 1
            colors[qry[1]] += 1
            balls[qry[0]] = qry[1]
            ans.append(c)
        return ans