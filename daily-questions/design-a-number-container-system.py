class NumberContainers:
    '''
        https://leetcode.com/problems/design-a-number-container-system/
    '''
    def __init__(self):
        self.indexToNum = {}
        self.numToIndices = {}

    def change(self, index: int, number: int) -> None:
        '''
            Time: O(logn)
        '''
        self.indexToNum[index] = number
        if number not in self.numToIndices:
            self.numToIndices[number] = []
        heapq.heappush(self.numToIndices[number], index)

    def find(self, number: int) -> int:
        '''
            Time: O(klogn)
        '''
        if number not in self.numToIndices:
            return -1
        pq = self.numToIndices[number]        
        while pq:
            currIndex = pq[0]
            if self.indexToNum[currIndex] != number:
                heapq.heappop(pq)
            else:
                return currIndex
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

"""
- number -> heap of indices
- index -> value at that index (to validate)
"""

class NumberContainers:
    def __init__(self):
        self.map_ = dict()
        self.rev_map = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        '''
            Time: O(logn)
        '''
        if index in self.map_:
            existing = self.map_[index]
            self.rev_map[existing].remove(index)
            if not bool(self.rev_map[existing]):
                self.rev_map.pop(existing)
            # n = len(self.rev_map[existing])
            # for i in range(n):
            #     if self.rev_map[existing][i] == index:
            #         self.rev_map[existing][i], self.rev_map[existing][-1] = self.rev_map[existing][-1], self.rev_map[existing][i]
            #         break
            # self.rev_map[existing].pop()
            # hq.heapify(self.rev_map[existing])
        self.map_[index] = number
        self.rev_map[number].add(index)

    def find(self, number: int) -> int:
        '''
            Time: O(1)
        '''
        return self.rev_map[number][0] if number in self.rev_map else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)