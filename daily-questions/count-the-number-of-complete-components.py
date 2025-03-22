from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
            https://leetcode.com/problems/count-the-number-of-complete-components
            Time: O(V+E)
            Space: O(V+E+n)
        '''
        adj_list = defaultdict(list)
        for [i, j] in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        seen = set()
        connected_comps = list()
        for i in range(n):
            if i not in seen:
                tmp = list()
                stk = [i]
                while stk:
                    vx = stk.pop()
                    tmp.append(vx)
                    seen.add(vx)
                    for neigh in adj_list[vx]:
                        if neigh not in seen:
                            stk.append(neigh)
                            seen.add(neigh)
                connected_comps.append(tmp)
        ans = 0
        for comp in connected_comps:
            tmp = 0
            for vx in comp:
                if len(adj_list[vx]) != len(comp) - 1:
                    tmp = 0
                    break
                else:
                    tmp = 1
            ans += tmp
        return ans
