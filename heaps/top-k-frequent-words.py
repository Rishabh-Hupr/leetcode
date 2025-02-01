import heapq as hq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
            https://leetcode.com/problems/top-k-frequent-words/description/
            Time: O(unique_frequencies log unique_frequencies) + O(unique_frequencies) + O(k log unique_frequencies)
            Space: O(unique_frequencies)
        '''
        c = Counter(words)
        store = defaultdict(list)
        for key, val in c.items():
            store[val].append(key)
            hq.heapify(store[val])
        hps = list()
        m = k
        for key, val in store.items():
            if m:
                hq.heappush(hps, key)
                m -= 1
            elif key > hps[0]:
                hq.heapreplace(hps, key)

        hps = [-i for i in hps]
        hq.heapify(hps)

        ans = list()
        while k and hps:
            x = hq.heappop(hps)
            while k and store[abs(x)]:
                if k:
                    ans.append(hq.heappop(store[abs(x)]))
                    k -= 1
        
        return ans
        
        '''
            Time: O(nlogn)
            Space: O(n)
        '''
        # hps = list()
        # m = k
        # for key, val in c.items():
        #     hq.heappush(hps, (-val, key))

        # ans = list()
        # while k:
        #     ans.append(hq.heappop(hps)[1])
        #     k -=1
        # return ans


        '''
            Time: O(nlogn)
            Space: O(n)
        '''
        # cnt=defaultdict(lambda :[0,""])
        # for i in words:
        #     cnt[i]=[cnt[i][0]-1,i]
        # lst=list(cnt.values())
        # lst=heapq.nsmallest(k,lst)
        # ans=[]
        # for i in lst:
        #     ans.append(i[1])
        # return ans
