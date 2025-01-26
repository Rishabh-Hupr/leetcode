import heapq as hq

class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        '''
            Time: O(n) + O(n) + O(n) + O(k) + O((n-k)logk) + O(n)
            Space: O(n) + O(n) + O(n) + O(n)
        '''
        c = Counter(arr)
        m = k
        hps = list()
        kees = list(c.keys())
        ref = defaultdict(list)
        for i in c:
            ref[c[i]].append(i)
        n = len(kees)
        for i in kees:
            if m:
                hps.append(c[i])
                m -= 1
            else:
                break
        hq.heapify(hps)
        for i in range(k, n):
            print("before", hps)
            if c[kees[i]] >= hps[0]:
                hq.heappushpop(hps, c[kees[i]])
            print("after", hps)
        ans = set()
        for i in hps:
            for ele in ref[i]:
                ans.add(ele)
        return list(ans)


        '''
            Time: O(n) + O(nlogk)
            Space: O(n)
        '''
        # counter = Counter(arr)
        # heap = []

        # for key, val in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (val, key))
        #     elif val > heap[0][0]:
        #         heapq.heappushpop(heap, (val, key))
        
        # return [h[1] for h in heap]

        '''
            Time: O(unique_frequencies) + O(klog(unique_frequencies))
            Space: O(n) + O(n)
        '''
        # c = Counter(arr)
        # n = defaultdict(list)
        # for i in c:
        #     n[c[i]].append(i)
        # del c
        # lis = list(n.keys())
        # new = [-x for x in lis]
        # heapq.heapify(new)
        # # print(n, new)
        # # for i in lis[k:]:
        # #     if i > new[0]:
        # #         heapq.heapreplace(new, i)
        # ans = []
        # while k:
        #     x = heapq.heappop(new)
        #     for i in n[abs(x)]:
        #         if k:
        #             ans.append(i)
        #             k -= 1
        #         else:
        #             return ans
        # return ans
