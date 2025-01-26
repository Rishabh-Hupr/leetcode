import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            Time: O(k) + O((n-k)logk) + O(k) + O(klogk) ~ O((n-k)logk)
            Space: O(n) + O(k) ~ O(n)
        '''
        def eud(x, y):
            return (x**2 + y**2)
        hps = list()
        n = len(points)
        m = k
        # store = defaultdict(list)
        # for i in points:
        #     if m:
        #         dist = eud(i[0], i[1])
        #         store[dist].append(tuple([i[0], i[1]]))
        #         hps.append(-dist)
        #         m -= 1
        # hq.heapify(hps)

        # for index in range(k, n):
        #     i, j = points[index][0], points[index][1]
        #     dist = eud(i, j)
        #     store[dist].append(tuple([i, j]))
        #     if dist < abs(hps[0]):
        #         hq.heapreplace(hps, -dist)
        # hps = [-x for x in hps]

        # hq.heapify(hps)
        # ans = list()
        
        # while k:
        #     dist = hq.heappop(hps)
        #     ans.extend(store[dist])
        #     k -= len(store[dist])
        
        # return ans
        

        '''
            Time: O(k) + O((n-k)log(k))
            Space: O(k)
        '''
        for i in points:
            if m:
                dist = eud(i[0], i[1])
                hps.append((-dist, i[0], i[1]))
                m -= 1
        hq.heapify(hps)

        for index in range(k, n):
            i, j = points[index][0], points[index][1]
            dist = eud(i, j)
            if dist < abs(hps[0][0]):
                hq.heapreplace(hps, (-dist, i, j))
        return [[i, j] for dist, i, j in hps]