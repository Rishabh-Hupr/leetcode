from collections import defaultdict
class Solution:
    def validPath(self, n: int, arr: List[List[int]], src: int, dst: int) -> bool:
        '''
            Time: O(E) + O(V+E) ~= O(V+E)
            Space: O(V) + O(V+E) + O(V) ~= O(V+E)
            Algo used is DFS
        '''
        if n==1:
            return True
        seen = set()
        seen.add(src)
        stk = list([src])
        adj_list = defaultdict(list)
        for u, v in arr:
            adj_list[u].append(v)
            adj_list[v].append(u)
        # print(adj_list)
        while stk:
            x = stk.pop()
            for neigh in adj_list[x]:
                if neigh == dst:
                    return True
                if neigh not in seen:
                    seen.add(neigh)
                    stk.append(neigh)
        return False
